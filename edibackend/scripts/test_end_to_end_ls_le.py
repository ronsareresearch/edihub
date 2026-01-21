"""
End-to-End Test Script for LS/LE Loop Processing
Date: 2026-01-21
Purpose: Process 1017_834_190831.edi and verify LS/LE loop data is captured correctly
"""
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834
from app.models.treo_models import (
    EnrollmentFile, EDIData, EDIAddtData,
    EDIControlSeg, EDITransSeg, ProcessLog
)
from sqlalchemy import func, text


def main():
    """Process 1017_834_190831.edi and verify LS/LE loop processing"""
    print("=" * 80)
    print("End-to-End Test: LS/LE Loop Processing")
    print("=" * 80)
    print(f"File: 1017_834_190831.edi")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Initialize database connection
    db = SessionLocalTreo()
    
    try:
        # Step 0: Clean up existing data and reset sequence
        print(f"\n0. Cleaning up existing data and resetting sequence...")
        print("-" * 80)
        
        # Truncate all data tables (in correct order due to foreign keys)
        tables_to_truncate = [
            'edi_addt_data',
            'edi_control_seg',
            'edi_data',
            'edi_trans_seg',
            'enrollment_files',
            'process_logs'
        ]
        
        for table in tables_to_truncate:
            try:
                db.execute(text(f"TRUNCATE TABLE public.{table} RESTART IDENTITY CASCADE"))
                print(f"   ✅ Truncated: {table}")
            except Exception as e:
                print(f"   ⚠️  Failed to truncate {table}: {str(e)}")
        
        # Reset enrollment_file_id sequence explicitly (in case RESTART IDENTITY didn't work)
        try:
            db.execute(text("SELECT setval('public.enrollment_files_enrollment_file_id_seq', 1, false)"))
            print(f"   ✅ Reset enrollment_file_id sequence to 1")
        except Exception as e:
            print(f"   ⚠️  Failed to reset sequence: {str(e)}")
        
        db.commit()
        print("-" * 80)
        print(f"   ✅ Cleanup complete - ready for fresh test")
        print()
    
    except Exception as e:
        print(f"   ❌ Cleanup failed: {str(e)}")
        db.rollback()
        return 1
    
    # Load EDI file
    edi_file_path = Path(__file__).parent.parent.parent / '1017_834_190831.edi'
    
    if not edi_file_path.exists():
        print(f"❌ ERROR: EDI file not found at {edi_file_path}")
        return 1
    
    print(f"\n1. Loading EDI file...")
    with open(edi_file_path, 'rb') as f:
        file_content = f.read()
    
    file_size = len(file_content)
    print(f"   File size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
    
    # Initialize parser
    print(f"\n1. Initializing parser...")
    print(f"   Client ID: 1")
    print(f"   LOB ID: 6")
    
    try:
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6
        )
        
        # Process file
        print(f"\n2. Processing EDI file...")
        print("   (This may take a few minutes for large files)")
        print("-" * 80)
        
        start_time = datetime.now()
        result = parser.parse_and_store(
            file_name='1017_834_190831.edi',
            file_content=file_content,
            created_by='test_end_to_end_ls_le'
        )
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        print("-" * 80)
        
        # Validate results
        print(f"\n3. Validation Results")
        print("=" * 80)
        
        if not result['success']:
            print(f"❌ Processing FAILED")
            print(f"   Error: {result.get('error_message', 'Unknown error')}")
            return 1
        
        print(f"✅ Processing SUCCESS")
        print(f"   Enrollment File ID: {result['enrollment_file_id']}")
        print(f"   Processing Time: {processing_time:.2f} seconds")
        print(f"   Throughput: {file_size / processing_time / 1024 / 1024:.2f} MB/s")
        
        enrollment_file_id = result['enrollment_file_id']
        
        # Check enrollment file record
        enrollment_file = db.query(EnrollmentFile).filter(
            EnrollmentFile.enrollment_file_id == enrollment_file_id
        ).first()
        
        if enrollment_file:
            print(f"\n✅ Enrollment File Record:")
            print(f"   File ID: {enrollment_file.enrollment_file_id}")
            print(f"   File Name: {enrollment_file.file_name}")
            print(f"   Processing Status: {enrollment_file.processing_status}")
        
        # Check EDI Control Segments
        edi_control_seg = db.query(EDIControlSeg).filter(
            EDIControlSeg.enrollment_file_id == enrollment_file_id
        ).first()
        
        if edi_control_seg:
            print(f"\n✅ EDI Control Segments:")
            print(f"   Enrollment File ID: {edi_control_seg.enrollment_file_id}")
            print(f"   ISA Segment: {edi_control_seg.isa01}-{edi_control_seg.isa16}")
            print(f"   GS Segment: {edi_control_seg.gs01}-{edi_control_seg.gs08}")
            print(f"   GE Segment: {edi_control_seg.ge01}-{edi_control_seg.ge02}")
            print(f"   IEA Segment: {edi_control_seg.iea01}-{edi_control_seg.iea02}")
        else:
            print(f"\n⚠️  EDI Control Segments: Not found")
        
        # Check EDI Transaction Segments
        edi_trans_seg_count = db.query(EDITransSeg).filter(
            EDITransSeg.enrollment_file_id == enrollment_file_id
        ).count()
        
        if edi_trans_seg_count > 0:
            print(f"\n✅ EDI Transaction Segments:")
            print(f"   Total Transaction Sets: {edi_trans_seg_count}")
            sample_trans = db.query(EDITransSeg).filter(
                EDITransSeg.enrollment_file_id == enrollment_file_id
            ).order_by(EDITransSeg.trans_index).limit(3).all()
            
            for trans in sample_trans:
                print(f"   Transaction #{trans.trans_index}:")
                print(f"      ST Segment: {trans.st01}-{trans.st02}-{trans.st03}")
                print(f"      BGN Segment: {trans.bgn01}-{trans.bgn02}")
                print(f"      SE Segment: {trans.se01}-{trans.se02}")
        else:
            print(f"\n⚠️  EDI Transaction Segments: Not found")
        
        # Check EDI Data (member records)
        edi_data_count = db.query(EDIData).filter(
            EDIData.enrollment_file_id == enrollment_file_id
        ).count()
        
        print(f"\n✅ EDI Data (Member Records):")
        print(f"   Total Members: {edi_data_count:,}")
        
        if edi_data_count > 0:
            # Sample a few members
            sample_members = db.query(EDIData).filter(
                EDIData.enrollment_file_id == enrollment_file_id
            ).order_by(EDIData.member_index).limit(3).all()
            
            print(f"\n   Sample Members:")
            for member in sample_members:
                print(f"      Member #{member.member_index}:")
                print(f"         INS01: {member.ins01}")
                print(f"         REF02_1 (Subscriber ID): {member.ref02_1}")
                print(f"         REF Count: {sum(1 for i in range(1, 13) if getattr(member, f'ref01_{i}', None))}")
                print(f"         DTP Count: {sum(1 for i in range(1, 11) if getattr(member, f'dtp01_{i}', None))}")
        
        # Check EDI Additional Data (LS/LE loops)
        edi_addt_data_count = db.query(EDIAddtData).filter(
            EDIAddtData.enrollment_file_id == enrollment_file_id
        ).count()
        
        print(f"\n✅ EDI Additional Data (LS/LE Loops):")
        print(f"   Total LS/LE Loops: {edi_addt_data_count:,}")
        
        if edi_addt_data_count > 0:
            # Sample a few LS/LE loops
            sample_loops = db.query(EDIAddtData).filter(
                EDIAddtData.enrollment_file_id == enrollment_file_id
            ).order_by(EDIAddtData.ref02_1, EDIAddtData.ls_le_index).limit(5).all()
            
            print(f"\n   Sample LS/LE Loops:")
            for loop in sample_loops:
                print(f"      Loop #{loop.ls_le_index} for Subscriber {loop.ref02_1}:")
                print(f"         LS01: {loop.ls01}")
                print(f"         LX01: {loop.lx01}")
                print(f"         N101: {loop.n101}, N102: {loop.n102}")
                print(f"         REF01: {loop.ref01}, REF02: {loop.ref02}")
                print(f"         DTP01: {loop.dtp01}, DTP02: {loop.dtp02}, DTP03: {loop.dtp03}")
                print(f"         LE01: {loop.le01}")
            
            # Check distribution of LS/LE loops per member
            loops_per_member = db.query(
                EDIAddtData.ref02_1,
                func.count(EDIAddtData.ls_le_index).label('loop_count')
            ).filter(
                EDIAddtData.enrollment_file_id == enrollment_file_id
            ).group_by(EDIAddtData.ref02_1).all()
            
            if loops_per_member:
                max_loops = max(count for _, count in loops_per_member)
                min_loops = min(count for _, count in loops_per_member)
                avg_loops = sum(count for _, count in loops_per_member) / len(loops_per_member)
                
                print(f"\n   LS/LE Loop Distribution:")
                print(f"      Members with LS/LE loops: {len(loops_per_member):,}")
                print(f"      Min loops per member: {min_loops}")
                print(f"      Max loops per member: {max_loops}")
                print(f"      Avg loops per member: {avg_loops:.2f}")
        else:
            print(f"\n⚠️  No LS/LE loops found in database")
            print(f"   This could mean:")
            print(f"   - The file doesn't contain LS/LE segments")
            print(f"   - The parser didn't capture them correctly")
            print(f"   - The service didn't populate the table")
        
        # Summary
        print(f"\n" + "=" * 80)
        print("VALIDATION SUMMARY")
        print("=" * 80)
        print(f"✅ Enrollment File: Created (ID: {enrollment_file_id})")
        print(f"✅ EDI Control Segments: {'Found' if edi_control_seg else 'Not found'}")
        print(f"✅ EDI Transaction Segments: {edi_trans_seg_count:,} records")
        print(f"✅ EDI Data (Members): {edi_data_count:,} records")
        print(f"✅ EDI Additional Data (LS/LE): {edi_addt_data_count:,} records")
        print(f"✅ Processing Time: {processing_time:.2f} seconds")
        print(f"\n" + "=" * 80)
        
        if edi_addt_data_count > 0:
            print("✅ TEST PASSED - LS/LE Loop Processing Working!")
        else:
            print("⚠️  TEST INCOMPLETE - No LS/LE loops found")
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
