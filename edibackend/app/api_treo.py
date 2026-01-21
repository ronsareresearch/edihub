"""
[TREO] - Treo Enrollment API Endpoints
Date: 2026-01-16
Purpose: RESTful API endpoints for Treo enrollment workflow
"""
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from datetime import datetime

from app.database_treo import get_db_treo
from app.services.treo_parser_834 import TreoParser834
from app.services.analytics.analytics_service import AnalyticsService
from app.models.treo_models import EnrollmentFile, ProcessLog
from sqlalchemy import text
from pathlib import Path
import json

router = APIRouter(tags=["Treo Enrollment"])  # Prefix set in main.py


@router.post("/enrollments/upload")
async def upload_enrollment_file(
    file: UploadFile = File(..., description="EDI 834 file to upload"),
    client_id: int = Form(..., description="Client ID"),
    lob_id: int = Form(..., description="Line of Business ID"),
    duplicate_mode: str = Form("warn", description="Duplicate handling: 'reject', 'warn', or 'allow'"),
    created_by: Optional[str] = Form(None, description="User who uploaded the file"),
    db: Session = Depends(get_db_treo)
):
    """
    Upload and process EDI 834 enrollment file.
    
    Workflow:
    1. Check for duplicate files
    2. Parse EDI file
    3. Apply all validations
    4. Build JSON structure
    5. Validate JSON schema
    6. Store in enrollment_files table (if valid)
    7. Log to process_log table
    
    Returns enrollment_file_id on success, error details on failure.
    """
    try:
        # Read file content
        file_content = await file.read()
        
        # Validate duplicate_mode
        if duplicate_mode not in ['reject', 'warn', 'allow']:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid duplicate_mode: {duplicate_mode}. Must be 'reject', 'warn', or 'allow'"
            )
        
        # Initialize parser
        parser = TreoParser834(
            db=db,
            client_id=client_id,
            lob_id=lob_id
        )
        
        # Parse and store
        result = parser.parse_and_store(
            file_name=file.filename or "unknown.edi",
            file_content=file_content,
            created_by=created_by
        )
        
        # Get error and warning counts from process_logs
        enrollment_file_id = result.get('enrollment_file_id')
        error_count = 0
        warning_count = 0
        duplicate_detected = False
        
        if enrollment_file_id:
            error_count = db.query(ProcessLog).filter(
                ProcessLog.enrollment_file_id == enrollment_file_id,
                ProcessLog.log_type == 'error'
            ).count()
            
            warning_count = db.query(ProcessLog).filter(
                ProcessLog.enrollment_file_id == enrollment_file_id,
                ProcessLog.log_type == 'warning'
            ).count()
            
            duplicate_detected = db.query(ProcessLog).filter(
                ProcessLog.enrollment_file_id == enrollment_file_id,
                ProcessLog.error_code == 'DUPLICATE_FILE_DETECTED'
            ).first() is not None
        
        if result['success']:
            return JSONResponse(
                status_code=201,
                content={
                    'success': True,
                    'enrollment_file_id': enrollment_file_id,
                    'message': 'File processed successfully',
                    'validation_results': {
                        'validation_status': 'valid',
                        'errors_count': error_count,
                        'warnings_count': warning_count,
                        'schema_validation': {
                            'is_valid': True,
                            'schema_version': '1.0'
                        }
                    },
                    'duplicate_detected': duplicate_detected,
                    'warnings': warning_count,
                    'errors': error_count
                }
            )
        else:
            return JSONResponse(
                status_code=400,
                content={
                    'success': False,
                    'enrollment_file_id': enrollment_file_id,
                    'message': result.get('error_message', 'Processing failed'),
                    'validation_results': {
                        'validation_status': 'invalid',
                        'errors_count': error_count,
                        'warnings_count': warning_count,
                        'schema_validation': {
                            'is_valid': False,
                            'schema_version': '1.0'
                        }
                    },
                    'duplicate_detected': duplicate_detected,
                    'errors': error_count,
                    'warnings': warning_count
                }
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )


@router.get("/enrollments/{enrollment_file_id}")
async def get_enrollment(
    enrollment_file_id: int,
    db: Session = Depends(get_db_treo)
):
    """
    Get enrollment file JSON by ID.
    
    Returns the complete EDI 834 JSON structure from the JSON file.
    Use this endpoint to retrieve the parsed JSON after file upload for display in the UI.
    """
    enrollment_file = db.query(EnrollmentFile).filter(
        EnrollmentFile.enrollment_file_id == enrollment_file_id
    ).first()
    
    if not enrollment_file:
        raise HTTPException(
            status_code=404,
            detail=f"Enrollment file not found: {enrollment_file_id}"
        )
    
    # Load JSON from file
    edi_data = None
    if enrollment_file.original_file_path:
        json_file_path = Path(__file__).parent.parent / enrollment_file.original_file_path
        if json_file_path.exists():
            try:
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    edi_data = json.load(f)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to load JSON file: {str(e)}"
                )
    
    return {
        'enrollment_file_id': enrollment_file.enrollment_file_id,
        'client_id': enrollment_file.client_id,
        'lob_id': enrollment_file.lob_id,
        'file_name': enrollment_file.file_name,
        'file_size_bytes': enrollment_file.file_size_bytes,
        'processing_status': enrollment_file.processing_status,
        'processed_at': enrollment_file.processed_at.isoformat() if enrollment_file.processed_at else None,
        'created_at': enrollment_file.created_at.isoformat(),
        'edi_data': edi_data
    }


@router.get("/enrollments/{enrollment_file_id}/json")
async def get_enrollment_json(
    enrollment_file_id: int,
    db: Session = Depends(get_db_treo)
):
    """
    Get enrollment file JSON data only (for UI display).
    
    Returns only the parsed JSON structure from the JSON file for easy display in the browser.
    This is a lightweight endpoint specifically for JSON viewing.
    """
    enrollment_file = db.query(EnrollmentFile).filter(
        EnrollmentFile.enrollment_file_id == enrollment_file_id
    ).first()
    
    if not enrollment_file:
        raise HTTPException(
            status_code=404,
            detail=f"Enrollment file not found: {enrollment_file_id}"
        )
    
    # Load JSON from file
    edi_data = {}
    if enrollment_file.original_file_path:
        json_file_path = Path(__file__).parent.parent / enrollment_file.original_file_path
        if json_file_path.exists():
            try:
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    edi_data = json.load(f)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to load JSON file: {str(e)}"
                )
    
    return JSONResponse(
        content=edi_data,
        headers={
            'Content-Type': 'application/json',
            'X-Enrollment-File-ID': str(enrollment_file_id),
            'X-File-Name': enrollment_file.file_name
        }
    )


@router.get("/enrollments/{enrollment_file_id}/logs")
async def get_enrollment_logs(
    enrollment_file_id: int,
    log_type: Optional[str] = Query(None, description="Filter by log type: 'error', 'warning', 'info', 'debug'"),
    db: Session = Depends(get_db_treo)
):
    """
    Get process logs for an enrollment file.
    
    Returns all logs (errors, warnings, info) associated with the enrollment file processing.
    """
    enrollment_file = db.query(EnrollmentFile).filter(
        EnrollmentFile.enrollment_file_id == enrollment_file_id
    ).first()
    
    if not enrollment_file:
        raise HTTPException(
            status_code=404,
            detail=f"Enrollment file not found: {enrollment_file_id}"
        )
    
    query = db.query(ProcessLog).filter(
        ProcessLog.enrollment_file_id == enrollment_file_id
    )
    
    if log_type:
        query = query.filter(ProcessLog.log_type == log_type)
    
    logs = query.order_by(ProcessLog.created_at.desc()).all()
    
    return {
        'enrollment_file_id': enrollment_file_id,
        'file_name': enrollment_file.file_name,
        'logs': [
            {
                'process_log_id': log.process_log_id,
                'log_type': log.log_type,
                'log_level': log.log_level,
                'message': log.message,
                'error_code': log.error_code,
                'segment_code': log.segment_code,
                'element_ref': log.element_ref,
                'line_number': log.line_number,
                'metadata': log.log_metadata,
                'created_at': log.created_at.isoformat()
            }
            for log in logs
        ],
        'total_logs': len(logs)
    }


@router.get("/enrollments")
async def list_enrollments(
    client_id: Optional[int] = Query(None, description="Filter by client ID"),
    lob_id: Optional[int] = Query(None, description="Filter by LOB ID"),
    processing_status: Optional[str] = Query(None, description="Filter by processing status"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    db: Session = Depends(get_db_treo)
):
    """
    List enrollment files with optional filters.
    
    Returns paginated list of enrollment files matching the criteria.
    """
    query = db.query(EnrollmentFile)
    
    if client_id:
        query = query.filter(EnrollmentFile.client_id == client_id)
    if lob_id:
        query = query.filter(EnrollmentFile.lob_id == lob_id)
    if processing_status:
        query = query.filter(EnrollmentFile.processing_status == processing_status)
    
    total = query.count()
    files = query.order_by(EnrollmentFile.created_at.desc()).offset(offset).limit(limit).all()
    
    return {
        'total': total,
        'limit': limit,
        'offset': offset,
        'enrollments': [
            {
                'enrollment_file_id': f.enrollment_file_id,
                'client_id': f.client_id,
                'lob_id': f.lob_id,
                'file_name': f.file_name,
                'file_size_bytes': f.file_size_bytes,
                'processing_status': f.processing_status,
                'processed_at': f.processed_at.isoformat() if f.processed_at else None,
                'created_at': f.created_at.isoformat()
            }
            for f in files
        ]
    }


@router.post("/enrollments/{enrollment_file_id}/query")
async def query_enrollment_json(
    enrollment_file_id: int,
    query_path: str = Form(..., description="JSON path query (e.g., 'transaction_set.bgn.bgn02')"),
    db: Session = Depends(get_db_treo)
):
    """
    Query JSON data using JSON path.
    
    Allows querying specific paths in the stored JSON structure from the JSON file.
    Example: query_path = "transaction_set.bgn.bgn02"
    """
    enrollment_file = db.query(EnrollmentFile).filter(
        EnrollmentFile.enrollment_file_id == enrollment_file_id
    ).first()
    
    if not enrollment_file:
        raise HTTPException(
            status_code=404,
            detail=f"Enrollment file not found: {enrollment_file_id}"
        )
    
    # Load JSON from file
    if not enrollment_file.original_file_path:
        raise HTTPException(
            status_code=404,
            detail=f"JSON file not found for enrollment file {enrollment_file_id}"
        )
    
    json_file_path = Path(__file__).parent.parent / enrollment_file.original_file_path
    if not json_file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"JSON file not found at {enrollment_file.original_file_path}"
        )
    
    # Load JSON and parse query path
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        parts = query_path.split('.')
        value = json_data
        for part in parts:
            if isinstance(value, dict):
                value = value.get(part)
            elif isinstance(value, list) and part.isdigit():
                value = value[int(part)] if int(part) < len(value) else None
            else:
                value = None
            if value is None:
                break
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid query path or JSON structure: {str(e)}"
        )
    
    return {
        'enrollment_file_id': enrollment_file_id,
        'query_path': query_path,
        'value': value
    }


@router.get("/enrollments/query/by-bgn-reference")
async def query_by_bgn_reference(
    bgn_ref_id: str = Query(..., description="BGN02 reference ID"),
    client_id: Optional[int] = Query(None, description="Filter by client ID"),
    lob_id: Optional[int] = Query(None, description="Filter by LOB ID"),
    db: Session = Depends(get_db_treo)
):
    """
    Query enrollment files by BGN02 reference ID.
    
    NOTE: This endpoint searches through JSON files, which may be slow for large datasets.
    Consider using the edi_trans_seg table for better performance.
    """
    # Get all enrollment files matching client/lob filters
    query = db.query(EnrollmentFile)
    
    if client_id:
        query = query.filter(EnrollmentFile.client_id == client_id)
    if lob_id:
        query = query.filter(EnrollmentFile.lob_id == lob_id)
    
    all_files = query.all()
    
    # Search through JSON files for matching BGN02
    matching_files = []
    base_path = Path(__file__).parent.parent
    
    for file in all_files:
        if not file.original_file_path:
            continue
        
        json_file_path = base_path / file.original_file_path
        if not json_file_path.exists():
            continue
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            # Check transaction_set.bgn.bgn02
            transaction_set = json_data.get('transaction_set', {})
            bgn_list = transaction_set.get('bgn', [])
            
            # Check if any BGN segment has matching bgn02
            for bgn in bgn_list if isinstance(bgn_list, list) else [bgn_list]:
                if isinstance(bgn, dict) and bgn.get('bgn02') == bgn_ref_id:
                    matching_files.append(file)
                    break
        except Exception:
            # Skip files that can't be read
            continue
    
    return {
        'bgn_ref_id': bgn_ref_id,
        'count': len(matching_files),
        'enrollments': [
            {
                'enrollment_file_id': f.enrollment_file_id,
                'file_name': f.file_name,
                'client_id': f.client_id,
                'lob_id': f.lob_id,
                'processed_at': f.processed_at.isoformat() if f.processed_at else None
            }
            for f in matching_files
        ]
    }


@router.get("/enrollments/query/by-member")
async def query_by_member(
    member_id: str = Query(..., description="Member identifier"),
    id_qualifier: Optional[str] = Query(None, description="REF qualifier (e.g., '0F', '1L')"),
    client_id: Optional[int] = Query(None, description="Filter by client ID"),
    lob_id: Optional[int] = Query(None, description="Filter by LOB ID"),
    db: Session = Depends(get_db_treo)
):
    """
    Query enrollment files containing a specific member.
    
    NOTE: This endpoint searches through the edi_data table for better performance.
    Uses ref02_1 (subscriber identifier) for member lookup.
    """
    # Use edi_data table for efficient member lookup
    from app.models.treo_models import EDIData
    from sqlalchemy import or_
    
    query = db.query(EnrollmentFile).join(
        EDIData, EnrollmentFile.enrollment_file_id == EDIData.enrollment_file_id
    ).filter(
        EDIData.ref02_1 == member_id
    )
    
    if id_qualifier:
        # Filter by REF qualifier (ref01)
        # Check all ref01_X columns for the qualifier
        qualifier_filters = []
        for i in range(1, 13):  # ref01_1 through ref01_12
            qualifier_filters.append(getattr(EDIData, f'ref01_{i}') == id_qualifier)
        
        query = query.filter(or_(*qualifier_filters))
    
    if client_id:
        query = query.filter(EnrollmentFile.client_id == client_id)
    if lob_id:
        query = query.filter(EnrollmentFile.lob_id == lob_id)
    
    files = query.distinct().all()
    
    return {
        'member_id': member_id,
        'id_qualifier': id_qualifier,
        'count': len(files),
        'enrollments': [
            {
                'enrollment_file_id': f.enrollment_file_id,
                'file_name': f.file_name,
                'client_id': f.client_id,
                'lob_id': f.lob_id,
                'processed_at': f.processed_at.isoformat() if f.processed_at else None
            }
            for f in files
        ]
    }


@router.get("/enrollments/{enrollment_file_id}/analytics")
async def get_enrollment_analytics(
    enrollment_file_id: int,
    db: Session = Depends(get_db_treo)
):
    """
    Get comprehensive analytics for a processed enrollment file.
    
    Returns detailed analytics including:
    - File information
    - Member statistics (total, unique, duplicates)
    - Duplicate analysis
    - Segment statistics
    - Transaction statistics
    - Additional data statistics (LS/LE loops)
    - Processing summary (errors, warnings, etc.)
    """
    try:
        analytics = AnalyticsService.get_file_analytics(
            db_session=db,
            enrollment_file_id=enrollment_file_id
        )
        return analytics
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate analytics: {str(e)}"
        )


@router.get("/analytics/summary")
async def get_summary_analytics(
    client_id: Optional[int] = Query(None, description="Filter by client ID"),
    lob_id: Optional[int] = Query(None, description="Filter by LOB ID"),
    db: Session = Depends(get_db_treo)
):
    """
    Get summary analytics across all processed files.
    
    Returns aggregate statistics including:
    - Total files processed
    - Total size
    - Total members processed
    - Unique members
    - Total transaction sets
    """
    try:
        analytics = AnalyticsService.get_summary_analytics(
            db_session=db,
            client_id=client_id,
            lob_id=lob_id
        )
        return analytics
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate summary analytics: {str(e)}"
        )
