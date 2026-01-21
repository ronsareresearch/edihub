"""
[TREO] - Analytics Service
Date: 2026-01-21
Purpose: Generate analytics for processed EDI 834 files
"""
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text, func
from datetime import datetime


class AnalyticsService:
    """
    Service to generate analytics for processed EDI 834 files.
    Provides insights into file processing, member data, duplicates, and more.
    """
    
    @staticmethod
    def get_file_analytics(
        db_session: Session,
        enrollment_file_id: int
    ) -> Dict[str, Any]:
        """
        Get comprehensive analytics for a processed enrollment file.
        
        Args:
            db_session: Database session
            enrollment_file_id: Enrollment file ID
            
        Returns:
            Dictionary containing analytics data
        """
        analytics = {
            'enrollment_file_id': enrollment_file_id,
            'file_info': {},
            'member_statistics': {},
            'duplicate_analysis': {},
            'segment_statistics': {},
            'transaction_statistics': {},
            'additional_data_statistics': {},
            'processing_summary': {}
        }
        
        # Get file info
        file_info_result = db_session.execute(
            text("""
                SELECT 
                    enrollment_file_id,
                    file_name,
                    file_size_bytes,
                    client_id,
                    lob_id,
                    processing_status,
                    processed_at,
                    created_at
                FROM public.enrollment_files
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        file_info = file_info_result.fetchone()
        
        if not file_info:
            raise ValueError(f"Enrollment file not found: {enrollment_file_id}")
        
        analytics['file_info'] = {
            'enrollment_file_id': file_info[0],
            'file_name': file_info[1],
            'file_size_bytes': file_info[2],
            'file_size_mb': round(file_info[2] / (1024 * 1024), 2) if file_info[2] else 0,
            'client_id': file_info[3],
            'lob_id': file_info[4],
            'processing_status': file_info[5],
            'processed_at': file_info[6].isoformat() if file_info[6] else None,
            'created_at': file_info[7].isoformat() if file_info[7] else None
        }
        
        # Member statistics
        member_stats_result = db_session.execute(
            text("""
                SELECT 
                    COUNT(*) as total_members,
                    COUNT(DISTINCT ref02_1) as unique_members,
                    COUNT(*) - COUNT(DISTINCT ref02_1) as duplicate_members_count
                FROM public.edi_data
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        member_stats = member_stats_result.fetchone()
        
        analytics['member_statistics'] = {
            'total_members_processed': member_stats[0] if member_stats else 0,
            'unique_members': member_stats[1] if member_stats else 0,
            'duplicate_members': member_stats[2] if member_stats else 0,
            'duplicate_percentage': round(
                (member_stats[2] / member_stats[0] * 100) if member_stats and member_stats[0] > 0 else 0,
                2
            )
        }
        
        # Duplicate analysis - detailed breakdown
        duplicate_analysis_result = db_session.execute(
            text("""
                SELECT 
                    ref02_1,
                    COUNT(*) as occurrence_count,
                    MIN(member_index) as first_occurrence,
                    MAX(member_index) as last_occurrence,
                    MAX(member_index) - MIN(member_index) as occurrence_span
                FROM public.edi_data
                WHERE enrollment_file_id = :file_id
                GROUP BY ref02_1
                HAVING COUNT(*) > 1
                ORDER BY COUNT(*) DESC
                LIMIT 20
            """),
            {'file_id': enrollment_file_id}
        )
        duplicate_details = []
        for row in duplicate_analysis_result:
            duplicate_details.append({
                'ref02_1': row[0],
                'occurrence_count': row[1],
                'first_occurrence_index': row[2],
                'last_occurrence_index': row[3],
                'occurrence_span': row[4]
            })
        
        analytics['duplicate_analysis'] = {
            'total_duplicate_members': len(duplicate_details),
            'max_occurrences': max([d['occurrence_count'] for d in duplicate_details], default=0),
            'duplicate_members': duplicate_details
        }
        
        # Segment statistics
        segment_stats_result = db_session.execute(
            text("""
                SELECT 
                    COUNT(*) as total_records,
                    COUNT(DISTINCT CASE WHEN ins01 IS NOT NULL THEN 1 END) as ins_segments,
                    COUNT(DISTINCT CASE WHEN nm101 IS NOT NULL THEN 1 END) as nm1_segments,
                    COUNT(DISTINCT CASE WHEN dmg01 IS NOT NULL THEN 1 END) as dmg_segments,
                    COUNT(DISTINCT CASE WHEN hd01_1 IS NOT NULL THEN 1 END) as hd_segments,
                    COUNT(DISTINCT CASE WHEN amt01 IS NOT NULL THEN 1 END) as amt_segments
                FROM public.edi_data
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        segment_stats = segment_stats_result.fetchone()
        
        analytics['segment_statistics'] = {
            'total_member_records': segment_stats[0] if segment_stats else 0,
            'ins_segments': segment_stats[1] if segment_stats else 0,
            'nm1_segments': segment_stats[2] if segment_stats else 0,
            'dmg_segments': segment_stats[3] if segment_stats else 0,
            'hd_segments': segment_stats[4] if segment_stats else 0,
            'amt_segments': segment_stats[5] if segment_stats else 0
        }
        
        # Transaction statistics
        trans_stats_result = db_session.execute(
            text("""
                SELECT 
                    COUNT(*) as total_transactions,
                    MIN(trans_index) as first_transaction,
                    MAX(trans_index) as last_transaction
                FROM public.edi_trans_seg
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        trans_stats = trans_stats_result.fetchone()
        
        analytics['transaction_statistics'] = {
            'total_transaction_sets': trans_stats[0] if trans_stats else 0,
            'first_transaction_index': trans_stats[1] if trans_stats else None,
            'last_transaction_index': trans_stats[2] if trans_stats else None
        }
        
        # Additional data statistics (LS/LE loops)
        addt_data_result = db_session.execute(
            text("""
                SELECT 
                    COUNT(*) as total_ls_le_loops,
                    COUNT(DISTINCT ref02_1) as members_with_ls_le,
                    MAX(ls_le_index) as max_ls_le_index_per_member
                FROM public.edi_addt_data
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        addt_data_stats = addt_data_result.fetchone()
        
        analytics['additional_data_statistics'] = {
            'total_ls_le_loops': addt_data_stats[0] if addt_data_stats else 0,
            'members_with_ls_le': addt_data_stats[1] if addt_data_stats else 0,
            'max_ls_le_index_per_member': addt_data_stats[2] if addt_data_stats else 0
        }
        
        # Processing summary
        process_logs_result = db_session.execute(
            text("""
                SELECT 
                    log_type,
                    COUNT(*) as count
                FROM public.process_log
                WHERE enrollment_file_id = :file_id
                GROUP BY log_type
            """),
            {'file_id': enrollment_file_id}
        )
        log_counts = {row[0]: row[1] for row in process_logs_result}
        
        analytics['processing_summary'] = {
            'total_logs': sum(log_counts.values()),
            'error_count': log_counts.get('error', 0),
            'warning_count': log_counts.get('warning', 0),
            'info_count': log_counts.get('info', 0),
            'debug_count': log_counts.get('debug', 0),
            'processing_status': file_info[5]
        }
        
        return analytics
    
    @staticmethod
    def get_summary_analytics(
        db_session: Session,
        client_id: Optional[int] = None,
        lob_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Get summary analytics across all processed files.
        
        Args:
            db_session: Database session
            client_id: Optional client ID filter
            lob_id: Optional LOB ID filter
            
        Returns:
            Dictionary containing summary analytics
        """
        filters = []
        params = {}
        
        if client_id:
            filters.append("ef.client_id = :client_id")
            params['client_id'] = client_id
        if lob_id:
            filters.append("ef.lob_id = :lob_id")
            params['lob_id'] = lob_id
        
        where_clause = f"WHERE {' AND '.join(filters)}" if filters else ""
        
        summary_result = db_session.execute(
            text(f"""
                SELECT 
                    COUNT(DISTINCT ef.enrollment_file_id) as total_files,
                    SUM(ef.file_size_bytes) as total_size_bytes,
                    COUNT(DISTINCT ed.member_index) as total_members,
                    COUNT(DISTINCT ed.ref02_1) as unique_members,
                    COUNT(DISTINCT ets.trans_index) as total_transactions
                FROM public.enrollment_files ef
                LEFT JOIN public.edi_data ed ON ef.enrollment_file_id = ed.enrollment_file_id
                LEFT JOIN public.edi_trans_seg ets ON ef.enrollment_file_id = ets.enrollment_file_id
                {where_clause}
            """),
            params
        )
        summary = summary_result.fetchone()
        
        return {
            'total_files_processed': summary[0] if summary else 0,
            'total_size_bytes': summary[1] if summary else 0,
            'total_size_mb': round((summary[1] or 0) / (1024 * 1024), 2),
            'total_members_processed': summary[2] if summary else 0,
            'unique_members': summary[3] if summary else 0,
            'total_transaction_sets': summary[4] if summary else 0
        }
