"""
Process EDI File Script
Date: 2026-01-20
Purpose: Simple script to process an EDI file through the parser
"""
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834
from app.models.treo_models import EnrollmentFile


def main():
    """Process an EDI file"""
    if len(sys.argv) < 2:
        print("Usage: python process_edi_file.py <file_name.edi> [naming_pattern]")
        print("\nExamples:")
        print("  python process_edi_file.py 1017_834.edi")
        print("  python process_edi_file.py 1017_834.edi '{file_id}_{file_name_stem}.json'")
        print("  python process_edi_file.py 1017_834.edi '{file_id}_{file_name_stem}_{file_hash_8}.json'")
        return 1
    
    file_name = sys.argv[1]
    naming_pattern = sys.argv[2] if len(sys.argv) > 2 else None
    
    print("=" * 80)
    print("Processing EDI File")
    print("=" * 80)
    print(f"File: {file_name}")
    if naming_pattern:
        print(f"Naming Pattern: {naming_pattern}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
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
        print(f"\n❌ ERROR: File not found. Checked:")
        for path in possible_paths:
            print(f"   - {path}")
        return 1
    
    # Load file
    print(f"\n1. Loading file...")
    with open(edi_file_path, 'rb') as f:
        file_content = f.read()
    
    file_size = len(file_content)
    print(f"   File size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
    
    # Initialize parser
    print(f"\n2. Initializing parser...")
    print(f"   Client ID: 1")
    print(f"   LOB ID: 6")
    
    db = SessionLocalTreo()
    try:
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6,
            json_naming_pattern=naming_pattern
        )
        
        # Process file
        print(f"\n3. Processing EDI file...")
        print("-" * 80)
        
        start_time = datetime.now()
        result = parser.parse_and_store(
            file_name=file_name,
            file_content=file_content,
            created_by='process_edi_file_script'
        )
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        print("-" * 80)
        
        # Display results
        print(f"\n4. Results")
        print("=" * 80)
        
        if result['success']:
            print(f"✅ Processing SUCCESS")
            print(f"   Enrollment File ID: {result['enrollment_file_id']}")
            print(f"   JSON File Path: {result['json_file_path']}")
            print(f"   Processing Time: {processing_time:.2f} seconds")
            print(f"   Throughput: {file_size / processing_time / 1024 / 1024:.2f} MB/s")
            
            # Verify file exists
            json_file_path = Path(__file__).parent.parent / result['json_file_path']
            if json_file_path.exists():
                json_size = json_file_path.stat().st_size
                print(f"\n   JSON File Details:")
                print(f"   - Path: {json_file_path}")
                print(f"   - Size: {json_size:,} bytes ({json_size/1024/1024:.2f} MB)")
                print(f"   - Exists: ✅")
            
            # Verify database record
            enrollment_file = db.query(EnrollmentFile).filter(
                EnrollmentFile.enrollment_file_id == result['enrollment_file_id']
            ).first()
            
            if enrollment_file:
                print(f"\n   Database Record:")
                print(f"   - File ID: {enrollment_file.enrollment_file_id}")
                print(f"   - File Name: {enrollment_file.file_name}")
                print(f"   - File Hash: {enrollment_file.file_hash[:16]}...")
                print(f"   - Processing Status: {enrollment_file.processing_status}")
                print(f"   - Original File Path: {enrollment_file.original_file_path}")
                print(f"   - Processed At: {enrollment_file.processed_at}")
            
            print(f"\n✅ File processed successfully!")
            print("=" * 80)
            return 0
        else:
            print(f"❌ Processing FAILED")
            print(f"   Error: {result.get('error_message', 'Unknown error')}")
            print(f"   File ID: {result.get('enrollment_file_id', 'N/A (no ID for failed files)')}")
            print("=" * 80)
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
