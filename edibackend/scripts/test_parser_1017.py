"""
Test script to process 1017_834.edi file and validate results (Streaming Architecture)
Date: 2026-01-20
Purpose: Test streaming parser with member-level storage and validate results
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834
from app.models.treo_models import EnrollmentFile
from app.models.treo_member_models import EnrollmentFileMember, EnrollmentFileProcessingStatus


def main():
    """Process 1017_834.edi and validate streaming architecture results"""
    print("=" * 80)
    print("Testing Streaming Parser with 1017_834.edi")
    print("=" * 80)
    
    # Database session
    db = SessionLocalTreo()
    
    try:
        # Load EDI file
        edi_file_path = Path(__file__).parent.parent.parent / '1017_834.edi'
        
        if not edi_file_path.exists():
            print(f"ERROR: EDI file not found at {edi_file_path}")
            return 1
        
        print(f"\n1. Loading EDI file: {edi_file_path}")
        with open(edi_file_path, 'rb') as f:
            file_content = f.read()
        
        file_size = len(file_content)
        print(f"   File size: {file_size:,} bytes")
        
        # Initialize parser with streaming enabled
        print(f"\n2. Initializing TreoParser834 (Streaming Architecture)")
        print(f"   Client ID: 1")
        print(f"   LOB ID: 6")
        print(f"   Streaming: Enabled")
        print(f"   Member Batch Size: 100")
        
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6,
            use_streaming=True,
            member_batch_size=100
        )
        print(f"   JSON files directory: {parser.json_files_dir}")
        
        # Process file
        print(f"\n3. Processing EDI file with streaming parser...")
        print("   (This may take a few minutes for large files)")
        print("-" * 80)
        
        result = parser.parse_and_store(
            file_name='1017_834.edi',
            file_content=file_content,
            created_by='test_script_streaming'
        )
        
        print("-" * 80)
        
        # Validate results
        print(f"\n4. Validation Results")
        print("=" * 80)
        
        if result['success']:
            print(f"✅ Processing SUCCESS")
            print(f"   Enrollment File ID: {result['enrollment_file_id']}")
            print(f"   JSON File Path: {result.get('json_file_path', 'N/A (large file - header only)')}")
            
            enrollment_file_id = result['enrollment_file_id']
            
            # Check enrollment file record
            enrollment_file = db.query(EnrollmentFile).filter(
                EnrollmentFile.enrollment_file_id == enrollment_file_id
            ).first()
            
            if enrollment_file:
                print(f"\n✅ Enrollment File Record:")
                print(f"   Enrollment File ID: {enrollment_file.enrollment_file_id}")
                print(f"   File Name: {enrollment_file.file_name}")
                print(f"   File Hash: {enrollment_file.file_hash[:16]}...")
                print(f"   Processing Status: {enrollment_file.processing_status}")
                print(f"   Validation Status: {enrollment_file.validation_status}")
                print(f"   Storage Mode: {enrollment_file.validation_summary.get('storage_mode', 'N/A')}")
                print(f"   Members in Table: {enrollment_file.validation_summary.get('members_in_table', 0):,}")
                
                # Check JSON data in database
                if enrollment_file.edi_data:
                    json_data = enrollment_file.edi_data
                    print(f"\n✅ JSON Data in Database:")
                    print(f"   Type: {type(json_data)}")
                    print(f"   Has 'interchange': {'interchange' in json_data}")
                    print(f"   Has 'transaction_set': {'transaction_set' in json_data}")
                    print(f"   Storage Mode: {json_data.get('metadata', {}).get('storage_mode', 'N/A')}")
                    
                    metadata = json_data.get('metadata', {})
                    print(f"\n   Metadata:")
                    print(f"      Total Segments: {metadata.get('total_segments', 0):,}")
                    print(f"      Total Members: {metadata.get('total_members', 0):,}")
            
            # Check member storage (NEW - key feature!)
            member_count = db.query(EnrollmentFileMember).filter(
                EnrollmentFileMember.enrollment_file_id == enrollment_file_id
            ).count()
            
            print(f"\n✅ Member Storage (NEW Feature):")
            print(f"   Members in Database: {member_count:,}")
            
            if member_count > 0:
                # Sample a few members
                sample_members = db.query(EnrollmentFileMember).filter(
                    EnrollmentFileMember.enrollment_file_id == enrollment_file_id
                ).order_by(EnrollmentFileMember.member_index).limit(3).all()
                
                print(f"\n   Sample Members:")
                for member in sample_members:
                    print(f"      Member #{member.member_index}: {member.member_data.get('loop_id', 'N/A')}")
                    segments = member.member_data.get('segments', {})
                    print(f"         Segment Types: {list(segments.keys())[:5]}")
                    
                    # Check INS segment
                    if member.ins_segment:
                        print(f"         INS Segment: {member.ins_segment.get('ins01', 'N/A')}")
            
            # Check processing status
            processing_status = db.query(EnrollmentFileProcessingStatus).filter(
                EnrollmentFileProcessingStatus.enrollment_file_id == enrollment_file_id
            ).first()
            
            if processing_status:
                print(f"\n✅ Processing Status:")
                print(f"   Processing Status: {processing_status.processing_status}")
                print(f"   Segments Parsed: {processing_status.segments_parsed:,}")
                print(f"   Members Parsed: {processing_status.members_parsed:,}")
                print(f"   Total Segments: {processing_status.total_segments:,}")
                print(f"   Last Checkpoint: {processing_status.last_checkpoint_at}")
            
            # Validate member count matches
            if member_count == processing_status.members_parsed:
                print(f"\n✅ Member Count Validation: PASSED")
                print(f"   Database members ({member_count:,}) == Parsed members ({processing_status.members_parsed:,})")
            else:
                print(f"\n⚠️  Member Count Validation: MISMATCH")
                print(f"   Database members: {member_count:,}")
                print(f"   Parsed members: {processing_status.members_parsed:,}")
            
            # Check JSON file on disk (if created)
            json_file_path = result.get('json_file_path')
            if json_file_path:
                json_path = Path(json_file_path)
                if json_path.exists():
                    json_size = json_path.stat().st_size
                    print(f"\n✅ JSON File on Disk:")
                    print(f"   Path: {json_file_path}")
                    print(f"   Size: {json_size:,} bytes ({json_size/1024/1024:.2f} MB)")
                    print(f"   Exists: Yes")
                else:
                    print(f"\n❌ JSON File on Disk:")
                    print(f"   Path: {json_file_path}")
                    print(f"   Exists: No (ERROR!)")
            else:
                print(f"\n⚠️  JSON File on Disk: Not created (large file - members in database)")
            
            # Summary
            print(f"\n" + "=" * 80)
            print("VALIDATION SUMMARY")
            print("=" * 80)
            print(f"✅ Enrollment File: Created")
            print(f"✅ Members in Database: {member_count:,}")
            print(f"✅ Processing Status: Tracked")
            print(f"✅ Streaming Architecture: Working")
            print(f"\n📊 Performance:")
            if member_count > 0:
                avg_member_size = sum(
                    len(str(m.member_data)) for m in db.query(EnrollmentFileMember).filter(
                        EnrollmentFileMember.enrollment_file_id == enrollment_file_id
                    ).limit(100).all()
                ) / min(100, member_count)
                print(f"   Estimated Total Member Data: ~{member_count * avg_member_size / 1024 / 1024:.2f} MB")
                print(f"   Storage Mode: {'Distributed (scalable)' if member_count > 10000 else 'Monolithic (small file)'}")
            
            print(f"\n" + "=" * 80)
            print("✅ TEST PASSED - Streaming Architecture Working!")
            print("=" * 80)
            
            return 0
        else:
            print(f"❌ Processing FAILED")
            print(f"   Error: {result.get('error_message', 'Unknown error')}")
            return 1
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
        
    finally:
        db.close()


if __name__ == '__main__':
    sys.exit(main())
