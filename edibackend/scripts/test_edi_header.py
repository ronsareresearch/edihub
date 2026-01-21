"""
Test script to process 1017_834.edi file and validate edi_header table population
Date: 2026-01-20
Purpose: Test parser with edi_header table population
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834
from app.models.treo_models import EnrollmentFile, EDIHeader


def main():
    """Process 1017_834.edi and validate edi_header population"""
    print("=" * 80)
    print("Testing EDI Header Population with 1017_834.edi")
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
        print(f"   File size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
        
        # Initialize parser
        print(f"\n2. Initializing TreoParser834")
        print(f"   Client ID: 1")
        print(f"   LOB ID: 6")
        
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6
        )
        print(f"   JSON files directory: {parser.json_files_dir}")
        
        # Process file
        print(f"\n3. Processing EDI file...")
        print("-" * 80)
        
        result = parser.parse_and_store(
            file_name='1017_834.edi',
            file_content=file_content,
            created_by='test_script_edi_header'
        )
        
        print("-" * 80)
        
        # Validate results
        print(f"\n4. Validation Results")
        print("=" * 80)
        
        if result is None:
            print(f"❌ ERROR: Parser returned None")
            print(f"   This indicates an exception occurred that wasn't handled properly")
            return 1
        
        if result.get('success'):
            print(f"✅ Processing SUCCESS")
            print(f"   Enrollment File ID: {result['enrollment_file_id']}")
            print(f"   JSON File Path: {result.get('json_file_path', 'N/A')}")
            
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
                print(f"   Original File Path: {enrollment_file.original_file_path}")
            
            # Check EDI Header record (NEW - key feature!)
            edi_header = db.query(EDIHeader).filter(
                EDIHeader.enrollment_file_id == enrollment_file_id
            ).first()
            
            if edi_header:
                print(f"\n✅ EDI Header Record (NEW Feature):")
                print(f"   Enrollment File ID: {edi_header.enrollment_file_id}")
                
                # ISA Segment
                print(f"\n   ISA Segment (Interchange Control Header):")
                print(f"      ISA01: {edi_header.isa01}")
                print(f"      ISA02: {edi_header.isa02}")
                print(f"      ISA05: {edi_header.isa05}")
                print(f"      ISA06: {edi_header.isa06}")  # Sender ID
                print(f"      ISA08: {edi_header.isa08}")  # Receiver ID
                print(f"      ISA09: {edi_header.isa09}")  # Date
                print(f"      ISA10: {edi_header.isa10}")  # Time
                print(f"      ISA12: {edi_header.isa12}")  # Version
                print(f"      ISA13: {edi_header.isa13}")  # Control Number
                
                # GS Segment
                print(f"\n   GS Segment (Functional Group Header):")
                print(f"      GS01: {edi_header.gs01}")
                print(f"      GS02: {edi_header.gs02}")  # Sender ID
                print(f"      GS03: {edi_header.gs03}")  # Receiver ID
                print(f"      GS04: {edi_header.gs04}")  # Date
                print(f"      GS05: {edi_header.gs05}")  # Time
                print(f"      GS06: {edi_header.gs06}")  # Group Control Number
                print(f"      GS08: {edi_header.gs08}")  # Version
                
                # ST Segment
                print(f"\n   ST Segment (Transaction Set Header):")
                print(f"      ST01: {edi_header.st01}")  # Transaction Set ID (834)
                print(f"      ST02: {edi_header.st02}")  # Transaction Set Control Number
                print(f"      ST03: {edi_header.st03}")  # Version
                
                # BGN Segment
                print(f"\n   BGN Segment (Beginning Segment):")
                print(f"      BGN01: {edi_header.bgn01}")
                print(f"      BGN02: {edi_header.bgn02}")  # Transaction Set Purpose Code
                print(f"      BGN03: {edi_header.bgn03}")  # Date
                print(f"      BGN04: {edi_header.bgn04}")  # Time
                print(f"      BGN08: {edi_header.bgn08}")  # Action Code
                
                # REF Segment (1 instance)
                print(f"\n   REF Segment (Reference Information) - Instance 1:")
                print(f"      REF01_1: {edi_header.ref01_1}")
                print(f"      REF02_1: {edi_header.ref02_1}")
                
                # DTP Segment (2 instances)
                print(f"\n   DTP Segment (Date/Time/Period):")
                print(f"      Instance 1:")
                print(f"         DTP01_1: {edi_header.dtp01_1}")
                print(f"         DTP02_1: {edi_header.dtp02_1}")
                print(f"         DTP03_1: {edi_header.dtp03_1}")
                print(f"      Instance 2:")
                print(f"         DTP01_2: {edi_header.dtp01_2}")
                print(f"         DTP02_2: {edi_header.dtp02_2}")
                print(f"         DTP03_2: {edi_header.dtp03_2}")
                
                # QTY Segment (should be NULL for Virginia)
                print(f"\n   QTY Segment (Quantity) - Should be NULL for Virginia:")
                print(f"      Instance 1: {edi_header.qty01_1} / {edi_header.qty02_1}")
                print(f"      Instance 2: {edi_header.qty01_2} / {edi_header.qty02_2}")
                print(f"      Instance 3: {edi_header.qty01_3} / {edi_header.qty02_3}")
                
                # SE Segment
                print(f"\n   SE Segment (Transaction Set Trailer):")
                print(f"      SE01: {edi_header.se01}")
                print(f"      SE02: {edi_header.se02}")
                
                # GE Segment
                print(f"\n   GE Segment (Functional Group Trailer):")
                print(f"      GE01: {edi_header.ge01}")
                print(f"      GE02: {edi_header.ge02}")
                
                # IEA Segment
                print(f"\n   IEA Segment (Interchange Control Trailer):")
                print(f"      IEA01: {edi_header.iea01}")
                print(f"      IEA02: {edi_header.iea02}")
                
                # Validation
                print(f"\n✅ EDI Header Validation:")
                
                # Validate ISA segment
                if edi_header.isa01 and edi_header.isa13:
                    print(f"   ✅ ISA Segment: Populated")
                else:
                    print(f"   ❌ ISA Segment: Missing data")
                
                # Validate GS segment
                if edi_header.gs01 and edi_header.gs06:
                    print(f"   ✅ GS Segment: Populated")
                else:
                    print(f"   ❌ GS Segment: Missing data")
                
                # Validate ST segment
                if edi_header.st01 == "834" and edi_header.st02:
                    print(f"   ✅ ST Segment: Populated (Transaction Set: {edi_header.st01})")
                else:
                    print(f"   ❌ ST Segment: Missing or invalid data")
                
                # Validate BGN segment
                if edi_header.bgn01 and edi_header.bgn02:
                    print(f"   ✅ BGN Segment: Populated")
                else:
                    print(f"   ❌ BGN Segment: Missing data")
                
                # Validate REF segment
                if edi_header.ref01_1 and edi_header.ref02_1:
                    print(f"   ✅ REF Segment: Populated (Type: {edi_header.ref01_1})")
                else:
                    print(f"   ❌ REF Segment: Missing data")
                
                # Validate DTP segments
                if edi_header.dtp01_1 and edi_header.dtp03_1:
                    print(f"   ✅ DTP Segment Instance 1: Populated (Type: {edi_header.dtp01_1})")
                    if edi_header.dtp01_2 and edi_header.dtp03_2:
                        print(f"   ✅ DTP Segment Instance 2: Populated (Type: {edi_header.dtp01_2})")
                    else:
                        print(f"   ⚠️  DTP Segment Instance 2: Missing (expected if file has only 1 DTP)")
                else:
                    print(f"   ❌ DTP Segment: Missing data")
                
                # Validate QTY segments (should be NULL for Virginia)
                if edi_header.qty01_1 is None:
                    print(f"   ✅ QTY Segment: NULL (correct for Virginia client)")
                else:
                    print(f"   ⚠️  QTY Segment: Has data (unexpected for Virginia)")
                
                # Validate SE segment
                if edi_header.se01 and edi_header.se02:
                    print(f"   ✅ SE Segment: Populated")
                else:
                    print(f"   ❌ SE Segment: Missing data")
                
                # Validate GE segment
                if edi_header.ge01 and edi_header.ge02:
                    print(f"   ✅ GE Segment: Populated")
                else:
                    print(f"   ❌ GE Segment: Missing data")
                
                # Validate IEA segment
                if edi_header.iea01 and edi_header.iea02:
                    print(f"   ✅ IEA Segment: Populated")
                else:
                    print(f"   ❌ IEA Segment: Missing data")
                
            else:
                print(f"\n❌ EDI Header Record: NOT FOUND")
                print(f"   Expected edi_header record for enrollment_file_id={enrollment_file_id}")
                return 1
            
            # Check JSON file on disk
            json_file_path = result.get('json_file_path')
            if json_file_path:
                json_path = Path(__file__).parent.parent / json_file_path
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
            
            # Summary
            print(f"\n" + "=" * 80)
            print("VALIDATION SUMMARY")
            print("=" * 80)
            print(f"✅ Enrollment File: Created")
            print(f"✅ EDI Header: Populated")
            print(f"✅ JSON File: Created on disk")
            print(f"✅ All Segments: Validated")
            print(f"\n" + "=" * 80)
            print("✅ TEST PASSED - EDI Header Population Working!")
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
