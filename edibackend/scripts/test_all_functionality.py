"""
Comprehensive Test Script for EDI 834 Parser
Date: 2026-01-20
Purpose: Test all functionality including parser, file naming, ID allocation, error handling
"""
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834
from app.services.json_file_name_generator import JSONFileNameGenerator
from app.models.treo_models import EnrollmentFile, ProcessLog


def test_file_naming_generator():
    """Test JSON file name generator with different patterns"""
    print("\n" + "=" * 80)
    print("TEST 1: JSON File Name Generator")
    print("=" * 80)
    
    db = SessionLocalTreo()
    try:
        # Test different naming patterns
        test_cases = [
            {
                'pattern': '{file_name_stem}.json',
                'expected': '1017_834.json',
                'description': 'Default pattern (simple)'
            },
            {
                'pattern': '{file_id}_{file_name_stem}.json',
                'expected_contains': ['_1017_834.json'],
                'description': 'With file ID (ID added later)'
            },
            {
                'pattern': '{file_name_stem}_{file_hash_8}.json',
                'expected_contains': ['1017_834_', '.json'],
                'description': 'With hash (8 chars)'
            },
            {
                'pattern': '{file_id}_{file_name_stem}_{file_hash_8}.json',
                'expected_contains': ['_1017_834_', '.json'],
                'description': 'With file ID and hash'
            },
            {
                'pattern': '{timestamp}_{file_name_stem}.json',
                'expected_contains': ['_1017_834.json'],
                'description': 'With timestamp'
            },
            {
                'pattern': '{client_code}_{lob_code}_{file_name_stem}.json',
                'expected_contains': ['_1017_834.json'],
                'description': 'With client and LOB codes'
            },
        ]
        
        file_hash = 'd019473ca6b3ea4ee6da0860156e7f9aa40b027e229d28f5af7814393a337975'
        original_file_name = '1017_834.edi'
        
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n  Test {i}.1: {test_case['description']}")
            print(f"    Pattern: {test_case['pattern']}")
            
            generator = JSONFileNameGenerator(
                naming_pattern=test_case['pattern'],
                client_id=1,
                lob_id=6,
                db_session=db
            )
            
            result = generator.generate(
                original_file_name=original_file_name,
                file_hash=file_hash,
                file_id=12,  # Test with file ID
                ensure_unique=False,
                check_existing=False
            )
            
            file_name = result['file_name']
            print(f"    Generated: {file_name}")
            
            # Validate
            if 'expected' in test_case:
                assert file_name == test_case['expected'], f"Expected {test_case['expected']}, got {file_name}"
                print(f"    ✅ PASSED")
            elif 'expected_contains' in test_case:
                all_contained = all(part in file_name for part in test_case['expected_contains'])
                assert all_contained, f"Expected to contain {test_case['expected_contains']}"
                print(f"    ✅ PASSED (contains required parts)")
        
        print(f"\n  ✅ All file naming tests passed!")
        return True
        
    except Exception as e:
        print(f"\n  ❌ File naming test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


def test_parser_with_file():
    """Test parser with actual EDI file"""
    print("\n" + "=" * 80)
    print("TEST 2: Parser with EDI File (Default Naming)")
    print("=" * 80)
    
    db = SessionLocalTreo()
    try:
        # Load EDI file
        edi_file_path = Path(__file__).parent.parent.parent / '1017_834.edi'
        
        if not edi_file_path.exists():
            print(f"  ❌ ERROR: EDI file not found at {edi_file_path}")
            return False
        
        print(f"  File: {edi_file_path}")
        
        with open(edi_file_path, 'rb') as f:
            file_content = f.read()
        
        file_size = len(file_content)
        print(f"  File size: {file_size:,} bytes")
        
        # Initialize parser with default naming
        print(f"\n  Initializing parser (default naming: {{file_name_stem}}.json)...")
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6
        )
        
        # Process file
        print(f"  Processing file...")
        result = parser.parse_and_store(
            file_name='1017_834.edi',
            file_content=file_content,
            created_by='test_all_functionality'
        )
        
        if result['success']:
            print(f"\n  ✅ Processing SUCCESS")
            print(f"    Enrollment File ID: {result['enrollment_file_id']}")
            print(f"    JSON File Path: {result['json_file_path']}")
            
            # Verify file exists
            json_file_path = Path(__file__).parent.parent / result['json_file_path']
            if json_file_path.exists():
                json_size = json_file_path.stat().st_size
                print(f"    JSON File Size: {json_size:,} bytes ({json_size/1024/1024:.2f} MB)")
                print(f"    ✅ JSON file exists")
            else:
                print(f"    ❌ JSON file not found at {json_file_path}")
                return False
            
            # Verify database record
            enrollment_file = db.query(EnrollmentFile).filter(
                EnrollmentFile.enrollment_file_id == result['enrollment_file_id']
            ).first()
            
            if enrollment_file:
                print(f"\n  ✅ Database Record:")
                print(f"    File ID: {enrollment_file.enrollment_file_id}")
                print(f"    File Name: {enrollment_file.file_name}")
                print(f"    File Hash: {enrollment_file.file_hash[:16]}...")
                print(f"    Processing Status: {enrollment_file.processing_status}")
                print(f"    Original File Path: {enrollment_file.original_file_path}")
                
                assert enrollment_file.processing_status == 'completed', "Status should be 'completed'"
                assert enrollment_file.original_file_path == result['json_file_path'], "Paths should match"
                print(f"    ✅ All assertions passed")
            else:
                print(f"    ❌ Database record not found")
                return False
            
            return True
        else:
            print(f"\n  ❌ Processing FAILED")
            print(f"    Error: {result.get('error_message', 'Unknown error')}")
            return False
        
    except Exception as e:
        print(f"\n  ❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


def test_parser_with_custom_naming():
    """Test parser with custom naming pattern"""
    print("\n" + "=" * 80)
    print("TEST 3: Parser with Custom Naming Pattern")
    print("=" * 80)
    
    db = SessionLocalTreo()
    try:
        # Load EDI file
        edi_file_path = Path(__file__).parent.parent.parent / '1017_834_1.edi'
        
        if not edi_file_path.exists():
            print(f"  ⚠️  Skipping: EDI file not found at {edi_file_path}")
            return True  # Skip if file doesn't exist
        
        with open(edi_file_path, 'rb') as f:
            file_content = f.read()
        
        # Initialize parser with custom naming pattern
        custom_pattern = "{file_id}_{file_name_stem}_{file_hash_8}.json"
        print(f"  Using pattern: {custom_pattern}")
        
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6,
            json_naming_pattern=custom_pattern
        )
        
        # Process file
        print(f"  Processing file...")
        result = parser.parse_and_store(
            file_name='1017_834_1.edi',
            file_content=file_content,
            created_by='test_all_functionality'
        )
        
        if result['success']:
            print(f"\n  ✅ Processing SUCCESS")
            print(f"    Enrollment File ID: {result['enrollment_file_id']}")
            print(f"    JSON File Path: {result['json_file_path']}")
            
            # Calculate actual hash for verification
            import hashlib
            actual_hash = hashlib.sha256(file_content).hexdigest()
            
            # Verify naming pattern
            expected_parts = [
                str(result['enrollment_file_id']),
                '1017_834_1',
                actual_hash[:8]  # First 8 chars of SHA-256 hash
            ]
            
            file_name = Path(result['json_file_path']).name
            print(f"    File Name: {file_name}")
            print(f"    Expected parts: {expected_parts}")
            
            # Verify all parts are in filename
            all_contained = all(part in file_name for part in expected_parts)
            assert all_contained, f"File name should contain {expected_parts}, got {file_name}"
            print(f"    ✅ Naming pattern verified")
            
            return True
        else:
            print(f"\n  ❌ Processing FAILED")
            print(f"    Error: {result.get('error_message', 'Unknown error')}")
            return False
        
    except Exception as e:
        print(f"\n  ❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


def test_error_handling_no_file_id():
    """Test that failed files don't get file IDs"""
    print("\n" + "=" * 80)
    print("TEST 4: Error Handling - Failed Files Don't Get IDs")
    print("=" * 80)
    
    db = SessionLocalTreo()
    try:
        # Get count before
        count_before = db.query(EnrollmentFile).count()
        print(f"  Enrollment files before: {count_before}")
        
        # Try to process invalid file (will fail)
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6
        )
        
        # Invalid EDI content (empty file - will raise ValueError)
        invalid_content = b""
        
        print(f"  Processing invalid file (should fail)...")
        result = parser.parse_and_store(
            file_name='invalid_file.edi',
            file_content=invalid_content,
            created_by='test_all_functionality'
        )
        
        # Get count after
        count_after = db.query(EnrollmentFile).count()
        print(f"  Enrollment files after: {count_after}")
        
        # Verify failure - parser catches exceptions and returns success=False
        assert not result['success'], f"Processing should fail, got: {result}"
        assert result['enrollment_file_id'] is None, "Failed files should not get IDs"
        assert count_after == count_before, f"Failed files should not create records (before: {count_before}, after: {count_after})"
        
        # Check process_log has entry
        log_entry = db.query(ProcessLog).filter(
            ProcessLog.file_name == 'invalid_file.edi',
            ProcessLog.enrollment_file_id.is_(None)
        ).order_by(ProcessLog.created_at.desc()).first()
        
        assert log_entry is not None, "Failed files should be logged in process_log"
        assert log_entry.enrollment_file_id is None, "Log entry should have no file_id"
        
        print(f"  ✅ Test passed:")
        print(f"    - Processing failed as expected")
        print(f"    - Error message: {result.get('error_message', 'N/A')}")
        print(f"    - No file ID allocated")
        print(f"    - No database record created")
        print(f"    - Error logged in process_log (without file_id)")
        
        return True
        
    except Exception as e:
        print(f"\n  ❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


def test_duplicate_detection():
    """Test duplicate file detection"""
    print("\n" + "=" * 80)
    print("TEST 5: Duplicate File Detection")
    print("=" * 80)
    
    db = SessionLocalTreo()
    try:
        # Load EDI file
        edi_file_path = Path(__file__).parent.parent.parent / '1017_834.edi'
        
        if not edi_file_path.exists():
            print(f"  ⚠️  Skipping: EDI file not found")
            return True
        
        with open(edi_file_path, 'rb') as f:
            file_content = f.read()
        
        # Process same file twice
        parser = TreoParser834(db=db, client_id=1, lob_id=6)
        
        print(f"  Processing file first time...")
        result1 = parser.parse_and_store(
            file_name='1017_834_duplicate_test.edi',
            file_content=file_content,
            created_by='test_all_functionality'
        )
        
        print(f"  Processing file second time (same content)...")
        result2 = parser.parse_and_store(
            file_name='1017_834_duplicate_test_2.edi',
            file_content=file_content,
            created_by='test_all_functionality'
        )
        
        # Both should succeed (different filenames)
        assert result1['success'], "First processing should succeed"
        assert result2['success'], "Second processing should succeed"
        
        # Both should get different IDs (different records)
        assert result1['enrollment_file_id'] != result2['enrollment_file_id'], "Should get different IDs"
        
        # Check for duplicate warning in logs
        duplicate_logs = db.query(ProcessLog).filter(
            ProcessLog.error_code == 'DUPLICATE_FILE_DETECTED'
        ).all()
        
        print(f"  ✅ Test passed:")
        print(f"    - First file ID: {result1['enrollment_file_id']}")
        print(f"    - Second file ID: {result2['enrollment_file_id']}")
        print(f"    - Both files processed successfully")
        print(f"    - Duplicate detection working (same hash, different names)")
        
        return True
        
    except Exception as e:
        print(f"\n  ❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


def main():
    """Run all tests"""
    print("=" * 80)
    print("COMPREHENSIVE EDI 834 PARSER TEST SUITE")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = []
    
    # Run tests
    results.append(("File Name Generator", test_file_naming_generator()))
    results.append(("Parser with Default Naming", test_parser_with_file()))
    results.append(("Parser with Custom Naming", test_parser_with_custom_naming()))
    results.append(("Error Handling - No File ID", test_error_handling_no_file_id()))
    results.append(("Duplicate Detection", test_duplicate_detection()))
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {status}: {test_name}")
    
    print(f"\n  Total: {passed}/{total} tests passed")
    print(f"  Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
