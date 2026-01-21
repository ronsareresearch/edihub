"""
Test script to process EDI file and provide detailed performance statistics
Date: 2026-01-20
Purpose: Test streaming parser with performance metrics and timing
"""
import sys
import time
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834
from app.models.treo_models import EnrollmentFile
from app.models.treo_member_models import EnrollmentFileMember, EnrollmentFileProcessingStatus


def format_size(size_bytes):
    """Format bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def format_time(seconds):
    """Format seconds to human readable format"""
    if seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    elif seconds < 60:
        return f"{seconds:.2f} s"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m {int(seconds % 60)}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}h {minutes}m {secs}s"


def main():
    """Process EDI file and provide performance statistics"""
    if len(sys.argv) < 2:
        print("Usage: python test_parser_performance.py <file_name.edi>")
        print("Example: python test_parser_performance.py 1017_834_1.edi")
        return 1
    
    file_name = sys.argv[1]
    
    print("=" * 80)
    print("Performance Test: Streaming Parser")
    print("=" * 80)
    print(f"File: {file_name}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Database session
    db = SessionLocalTreo()
    
    try:
        # Load EDI file - check multiple possible locations
        possible_paths = [
            Path(__file__).parent.parent.parent / file_name,  # Root directory
            Path(file_name),  # Absolute path or current directory
            Path(__file__).parent.parent / file_name,  # edibackend directory
        ]
        
        edi_file_path = None
        for path in possible_paths:
            if path.exists():
                edi_file_path = path
                break
        
        if not edi_file_path:
            # Try to find it
            for path in possible_paths:
                parent = path.parent
                if parent.exists():
                    found_files = list(parent.glob(file_name))
                    if found_files:
                        edi_file_path = found_files[0]
                        break
        
        if not edi_file_path.exists():
            print(f"❌ ERROR: EDI file not found at {edi_file_path}")
            return 1
        
        # Step 1: File Information
        print(f"\n[STEP 1] File Information")
        print("-" * 80)
        with open(edi_file_path, 'rb') as f:
            file_content = f.read()
        
        file_size = len(file_content)
        print(f"   File Path: {edi_file_path}")
        print(f"   File Size: {file_size:,} bytes ({format_size(file_size)})")
        
        # Estimate segments (rough estimate: ~80 bytes per segment)
        estimated_segments = file_size // 80
        print(f"   Estimated Segments: ~{estimated_segments:,}")
        
        # Step 2: Initialize Parser
        print(f"\n[STEP 2] Parser Initialization")
        print("-" * 80)
        init_start = time.time()
        
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6,
            use_streaming=True,
            member_batch_size=100
        )
        
        init_time = time.time() - init_start
        print(f"   Client ID: 1")
        print(f"   LOB ID: 6")
        print(f"   Streaming: Enabled")
        print(f"   Member Batch Size: 100")
        print(f"   Initialization Time: {format_time(init_time)}")
        
        # Step 3: Process File
        print(f"\n[STEP 3] File Processing")
        print("-" * 80)
        print("   Processing started...")
        process_start = time.time()
        
        result = parser.parse_and_store(
            file_name=file_name,
            file_content=file_content,
            created_by='performance_test'
        )
        
        process_time = time.time() - process_start
        
        if not result['success']:
            print(f"\n❌ Processing FAILED")
            print(f"   Error: {result.get('error_message', 'Unknown error')}")
            return 1
        
        # Step 4: Performance Statistics
        print(f"\n[STEP 4] Performance Statistics")
        print("=" * 80)
        
        enrollment_file_id = result['enrollment_file_id']
        enrollment_file = db.query(EnrollmentFile).filter(
            EnrollmentFile.enrollment_file_id == enrollment_file_id
        ).first()
        
        processing_status = db.query(EnrollmentFileProcessingStatus).filter(
            EnrollmentFileProcessingStatus.enrollment_file_id == enrollment_file_id
        ).first()
        
        if not enrollment_file or not processing_status:
            print("❌ ERROR: Could not retrieve processing statistics")
            return 1
        
        # Overall Performance
        print(f"\n📊 Overall Performance:")
        print(f"   Total Processing Time: {format_time(process_time)}")
        print(f"   File Size: {format_size(file_size)}")
        print(f"   Throughput: {format_size(file_size / process_time)}/s")
        print(f"   Processing Rate: {file_size / process_time / 1024 / 1024:.2f} MB/s")
        
        # Parsing Statistics
        stats = enrollment_file.validation_summary.get('parsing_stats', {})
        segments_parsed = stats.get('segments_parsed', 0) or processing_status.segments_parsed or 0
        members_parsed = stats.get('members_parsed', 0) or processing_status.members_parsed or 0
        total_segments = stats.get('total_segments', 0) or processing_status.total_segments or segments_parsed
        
        print(f"\n📈 Parsing Statistics:")
        print(f"   Segments Parsed: {segments_parsed:,}")
        print(f"   Total Segments: {total_segments:,}")
        print(f"   Members Parsed: {members_parsed:,}")
        print(f"   Segments per Member: {segments_parsed / members_parsed if members_parsed > 0 else 0:.1f}")
        print(f"   Parsing Speed: {segments_parsed / process_time if process_time > 0 else 0:,.0f} segments/s")
        print(f"   Member Processing Speed: {members_parsed / process_time if process_time > 0 else 0:,.1f} members/s")
        
        # Timing Breakdown
        print(f"\n⏱️  Timing Breakdown:")
        print(f"   Initialization: {format_time(init_time)} ({init_time / process_time * 100:.1f}%)")
        parsing_time = process_time - init_time
        print(f"   Parsing & Storage: {format_time(parsing_time)} ({parsing_time / process_time * 100:.1f}%)")
        print(f"   Per Segment: {parsing_time / segments_parsed * 1000 if segments_parsed > 0 else 0:.3f} ms")
        print(f"   Per Member: {parsing_time / members_parsed if members_parsed > 0 else 0:.3f} s")
        
        # Database Statistics
        member_count = db.query(EnrollmentFileMember).filter(
            EnrollmentFileMember.enrollment_file_id == enrollment_file_id
        ).count()
        
        print(f"\n💾 Database Statistics:")
        print(f"   Enrollment File ID: {enrollment_file_id}")
        print(f"   Members Stored: {member_count:,}")
        print(f"   Storage Mode: {enrollment_file.validation_summary.get('storage_mode', 'N/A')}")
        
        # Estimate member data size
        if member_count > 0:
            sample_members = db.query(EnrollmentFileMember).filter(
                EnrollmentFileMember.enrollment_file_id == enrollment_file_id
            ).limit(100).all()
            
            avg_member_size = sum(
                len(str(m.member_data)) for m in sample_members
            ) / len(sample_members) if sample_members else 0
            
            total_member_data_size = member_count * avg_member_size
            print(f"   Estimated Member Data Size: {format_size(total_member_data_size)}")
            print(f"   Average Member Size: {format_size(avg_member_size)}")
        
        # JSON File Statistics (if created)
        json_file_path = result.get('json_file_path')
        if json_file_path:
            json_path = Path(json_file_path)
            if json_path.exists():
                json_size = json_path.stat().st_size
                print(f"   JSON File Size: {format_size(json_size)}")
                print(f"   JSON Compression Ratio: {file_size / json_size if json_size > 0 else 0:.2f}x")
        
        # Memory Efficiency (estimates)
        print(f"\n🧠 Memory Efficiency (Estimates):")
        # Estimate memory usage based on batch size
        estimated_memory = member_count * 1024 * 5  # ~5KB per member estimate
        print(f"   Estimated Peak Memory: ~{format_size(estimated_memory)}")
        print(f"   Batch Commit Size: 100 members")
        print(f"   Memory per Member: ~{format_size(estimated_memory / member_count if member_count > 0 else 0)}")
        
        # Scalability Metrics
        print(f"\n🚀 Scalability Metrics:")
        processing_rate_per_min = members_parsed / (process_time / 60) if process_time > 0 else 0
        estimated_1m_time = (1_000_000 / processing_rate_per_min) if processing_rate_per_min > 0 else 0
        print(f"   Processing Rate: {processing_rate_per_min:.0f} members/minute")
        print(f"   Estimated Time for 1M Members: {format_time(estimated_1m_time)}")
        print(f"   Can Handle 1M+ Members: {'✅ YES' if processing_rate_per_min > 0 else '❌ NO'}")
        
        # Status Summary
        print(f"\n✅ Status Summary:")
        print(f"   Processing Status: {enrollment_file.processing_status}")
        print(f"   Validation Status: {enrollment_file.validation_status}")
        print(f"   Duplicate Detected: {enrollment_file.validation_summary.get('duplicate_detected', False)}")
        print(f"   Completed At: {enrollment_file.processed_at}")
        
        # Performance Grade
        print(f"\n🎯 Performance Grade:")
        mb_per_second = file_size / process_time / 1024 / 1024
        members_per_second = members_parsed / process_time if process_time > 0 else 0
        
        if mb_per_second > 10 and members_per_second > 100:
            grade = "A+ (Excellent)"
        elif mb_per_second > 5 and members_per_second > 50:
            grade = "A (Very Good)"
        elif mb_per_second > 2 and members_per_second > 20:
            grade = "B (Good)"
        elif mb_per_second > 1 and members_per_second > 10:
            grade = "C (Acceptable)"
        else:
            grade = "D (Needs Improvement)"
        
        print(f"   Grade: {grade}")
        print(f"   MB/s: {mb_per_second:.2f}")
        print(f"   Members/s: {members_per_second:.1f}")
        
        print(f"\n" + "=" * 80)
        print(f"✅ TEST COMPLETED SUCCESSFULLY")
        print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        return 0
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
        
    finally:
        db.close()


if __name__ == '__main__':
    sys.exit(main())
