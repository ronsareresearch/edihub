"""
[TREO] - Treo EDI 834 Parser Service (Simplified Architecture)
Date: 2026-01-20
Purpose: Parse EDI 834 files and save as JSON files
Workflow:
    1. Calculate file hash
    2. Parse EDI file using TreoStreamingParser834
    3. Create JSON file and save to data/json_files/ directory
    4. Store file metadata in enrollment_files table (no data storage)
    5. Log processing results to process_log table
"""
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from datetime import datetime
from pathlib import Path
import hashlib
import json

from app.services.treo_streaming_parser_834 import TreoStreamingParser834
from app.services.json_file_name_generator import JSONFileNameGenerator
from app.services.edi_control_seg_service import EDIControlSegService
from app.services.edi_trans_seg_service import EDITransSegService
from app.services.edi_data_service import EDIDataService
from app.services.edi_addt_data_service import EDIAddtDataService
from app.models.treo_models import EnrollmentFile, ProcessLog


class TreoParser834:
    """
    Treo EDI 834 Parser Service (Simplified Architecture)
    
    Workflow:
    1. Calculate file hash
    2. Parse EDI file using streaming parser
    3. Create JSON file and save to data/json_files/ directory
    4. Store file metadata in enrollment_files table (no data storage)
    5. Log processing results to process_log table
    """
    
    def __init__(
        self,
        db: Session,
        client_id: int,
        lob_id: int,
        json_files_dir: Optional[str] = None,
        json_naming_pattern: Optional[str] = None
    ):
        """
        Initialize Treo parser.
        
        Args:
            db: Treo database session
            client_id: Client ID
            lob_id: Line of Business ID
            json_files_dir: Optional directory for storing JSON files (default: data/json_files/)
            json_naming_pattern: Optional JSON file naming pattern (default: "{file_name_stem}.json")
                                 Supports placeholders: file_id, file_hash, file_hash_8, timestamp, etc.
        """
        self.db = db
        self.client_id = client_id
        self.lob_id = lob_id
        
        # Set up JSON files directory (simple path, no client/lob subdirectories)
        if json_files_dir:
            self.json_files_dir = Path(json_files_dir)
        else:
            # Default: data/json_files/
            base_path = Path(__file__).parent.parent.parent
            self.json_files_dir = base_path / 'data' / 'json_files'
        
        # Create directory if it doesn't exist
        self.json_files_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize JSON file name generator
        self.file_name_generator = JSONFileNameGenerator(
            naming_pattern=json_naming_pattern,
            client_id=client_id,
            lob_id=lob_id,
            db_session=db,
            json_files_dir=self.json_files_dir
        )
    
    @staticmethod
    def calculate_file_hash(file_content: bytes) -> str:
        """Calculate SHA-256 hash of file content."""
        return hashlib.sha256(file_content).hexdigest()
    
    def parse_and_store(
        self,
        file_name: str,
        file_content: bytes,
        created_by: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Complete workflow: Parse EDI file, create JSON file, store file metadata.
        
        Args:
            file_name: Name of uploaded file
            file_content: File content as bytes
            created_by: User who uploaded the file
            
        Returns:
            Dict with processing results:
            {
                'success': bool,
                'enrollment_file_id': Optional[int],
                'json_file_path': Optional[str],
                'error_message': Optional[str]
            }
        """
        file_hash = None
        try:
            # Step 1: Calculate file hash
            file_hash = self.calculate_file_hash(file_content)
            self._log_info(
                file_name=file_name,
                file_hash=file_hash,
                message=f"Starting file processing: {file_name}",
                error_code='FILE_PROCESSING_STARTED'
                )
            
            # Step 2: Check for duplicate files (only check successfully processed files)
            duplicate_check = self._check_duplicate(file_hash)
            if duplicate_check['is_duplicate']:
                self._log_warning(
                    file_name=file_name,
                    file_hash=file_hash,
                    message=f"Duplicate file detected: {duplicate_check['message']}",
                    error_code='DUPLICATE_FILE_DETECTED',
                    enrollment_file_id=duplicate_check.get('existing_file_id')
                )
            
            # Step 3: Parse EDI file using streaming parser
            # IMPORTANT: We parse FIRST, then create EnrollmentFile record only on success
            # This ensures only successfully processed files get IDs
            x12_content = file_content.decode('utf-8')
            
            streaming_parser = TreoStreamingParser834(
                db_session=self.db,
                client_id=self.client_id,
                lob_id=self.lob_id,
                file_hash=file_hash,
                member_batch_size=100
            )
            
            # Parse file (no member callbacks - just build JSON structure)
            parse_result = streaming_parser.parse_x12_file_streaming(
                        file_name=file_name,
                x12_content=x12_content,
                member_callback=None,  # No member storage
                progress_callback=None  # No progress tracking needed
            )
            
            if not parse_result.get('success'):
                # Parsing failed - log error WITHOUT creating EnrollmentFile record
                # This ensures failed files don't consume database IDs
                error_msg = parse_result.get('error_message', 'Parsing failed')
                self._log_error(
                    file_name=file_name,
                    file_hash=file_hash,
                    enrollment_file_id=None,  # No file ID for failed files
                    message=f"Parsing failed: {error_msg}",
                    error_code='PARSING_FAILED',
                    metadata={'parsing_error': error_msg}
                    )
                
                self.db.commit()
                
                return {
                    'success': False,
                    'enrollment_file_id': None,  # No ID allocated for failed files
                    'json_file_path': None,
                    'error_message': error_msg
                }
            
            # Step 4: Build JSON structure from parsed data (includes full loops structure)
            header_data = parse_result.get('header_data', {})
            stats = parse_result.get('stats', {})
            
            # JSON structure already includes all loops from streaming parser
            json_data = {
                'interchange': header_data.get('interchange', {}),
                'functional_group': header_data.get('functional_group', {}),
                'transaction_set': header_data.get('transaction_set', {}),
                'loops': header_data.get('loops', []),  # Full loops with all members
                'metadata': {
                    'total_segments': stats.get('segments_parsed', 0),
                    'total_members': stats.get('members_parsed', 0),
                    'storage_mode': 'file_only'  # Data stored in JSON file, not database
                }
                }
            
            # Step 5: Create JSON file on disk using file name generator
            # Generate JSON file name using configured naming pattern (without file_id yet)
            file_name_result = self.file_name_generator.generate(
                original_file_name=file_name,
                file_hash=file_hash,
                file_id=None,  # File ID not yet created (will be created after all processing)
                ensure_unique=True,
                check_existing=True
            )
            
            json_file_name = file_name_result['file_name']
            relative_path = file_name_result['relative_path']
            json_file_path = Path(file_name_result['absolute_path'])
            
            # Write JSON file
            try:
                with open(json_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(json_data, json_file, indent=2, ensure_ascii=False)
                
                json_file_size = json_file_path.stat().st_size
                
            except Exception as e:
                # JSON file creation failed - log error and abort (no file ID)
                self._log_error(
                    file_name=file_name,
                    file_hash=file_hash,
                    enrollment_file_id=None,  # No file ID allocated
                    message=f"Failed to create JSON file: {str(e)}",
                    error_code='JSON_FILE_CREATION_FAILED',
                    metadata={'json_file_path': str(json_file_path), 'error': str(e)}
                )
                self.db.commit()
                
                return {
                    'success': False,
                    'enrollment_file_id': None,  # No ID for failed files
                    'json_file_path': None,
                    'error_message': f"JSON file creation failed: {str(e)}"
                }
            
            # Step 6: Create enrollment file record EARLY with status='processing'
            # This consumes the sequence ID immediately, preventing gaps
            # If processing fails, we'll update status to 'failed' instead of rolling back
            enrollment_file = EnrollmentFile(
                client_id=self.client_id,
                lob_id=self.lob_id,
                file_name=file_name,
                file_size_bytes=len(file_content),
                file_hash=file_hash,
                original_file_path=relative_path,
                processing_status='processing',  # Will be updated to 'completed' on success
                processed_at=None,  # Will be set on success
                created_by=created_by
            )
            self.db.add(enrollment_file)
            self.db.flush()  # Get enrollment_file_id - sequence is consumed here
            
            # Step 7: Populate all data tables with the enrollment_file_id
            # If any step fails, the outer exception handler will update enrollment_file status to 'failed'
            # This ensures the ID is still used (no gap) and we have a record of the failure
            
            # Step 7a: Populate edi_control_seg table with file-level control segments (ISA, GS, GE, IEA)
            EDIControlSegService.populate_from_json(
                db_session=self.db,
                enrollment_file_id=enrollment_file.enrollment_file_id,
                json_data=json_data
            )
            
            # Step 7b: Populate edi_trans_seg table with transaction-level segments (ST, BGN, REF, DTP, N1, SE)
            EDITransSegService.populate_from_json(
                db_session=self.db,
                enrollment_file_id=enrollment_file.enrollment_file_id,
                json_data=json_data
            )
            
            # Step 7c: Populate edi_data table with flattened member-level data
            EDIDataService.populate_from_json(
                db_session=self.db,
                enrollment_file_id=enrollment_file.enrollment_file_id,
                json_data=json_data
            )
            
            # Step 7d: Populate edi_addt_data table with Additional Reporting Categories (LS/LE loops)
            EDIAddtDataService.populate_from_json(
                db_session=self.db,
                enrollment_file_id=enrollment_file.enrollment_file_id,
                json_data=json_data
            )
            
            # Step 8: Update enrollment_file status to 'completed' now that all processing succeeded
            enrollment_file.processing_status = 'completed'
            enrollment_file.processed_at = datetime.utcnow()
            
            # Step 9: Optional: Rename JSON file to include file_id if pattern requires it
            # (Only if pattern includes {file_id} placeholder and file was created before ID was known)
            if '{file_id}' in self.file_name_generator.naming_pattern:
                # Regenerate with actual file_id
                updated_file_name_result = self.file_name_generator.generate(
                    original_file_name=file_name,
                    file_hash=file_hash,
                    file_id=enrollment_file.enrollment_file_id,
                    ensure_unique=False,  # Don't check again since we're renaming
                    check_existing=False
                )
                
                new_json_file_name = updated_file_name_result['file_name']
                new_relative_path = updated_file_name_result['relative_path']
                new_json_file_path = Path(updated_file_name_result['absolute_path'])
                
                # Rename file if different
                if new_json_file_name != json_file_name and new_json_file_path != json_file_path:
                    try:
                        json_file_path.rename(new_json_file_path)
                        relative_path = new_relative_path
                        json_file_name = new_json_file_name
                        enrollment_file.original_file_path = relative_path
                    except Exception as e:
                        # Log warning but continue - file exists with original name
                        self._log_warning(
                            file_name=file_name,
                            file_hash=file_hash,
                            enrollment_file_id=enrollment_file.enrollment_file_id,
                            message=f"Failed to rename JSON file to include file_id: {str(e)}",
                            error_code='JSON_FILE_RENAME_FAILED',
                            metadata={'original_name': json_file_name, 'new_name': new_json_file_name}
                        )
            
            # Step 10: Log successful processing (with file ID)
            self._log_info(
                file_name=file_name,
                file_hash=file_hash,
                enrollment_file_id=enrollment_file.enrollment_file_id,  # File ID allocated on success
                message=f"File processed successfully. Segments parsed: {stats.get('segments_parsed', 0)}, Members parsed: {stats.get('members_parsed', 0)}",
                error_code='FILE_PROCESSING_SUCCESS',
                metadata={
                    'parsing_stats': stats,
                    'duplicate_detected': duplicate_check['is_duplicate'],
                    'json_file_path': relative_path,
                    'json_file_size_bytes': json_file_size
                }
            )
            
            # Step 11: Commit transaction after all processing succeeds
            # The enrollment_file_id sequence was consumed early, so even if we had failures,
            # the ID is preserved by updating status to 'failed' instead of rolling back
            self.db.commit()
            
            return {
                'success': True,
                'enrollment_file_id': enrollment_file.enrollment_file_id,
                'json_file_path': relative_path,
                'error_message': None
            }
            
        except Exception as e:
            # Check if enrollment_file was created (sequence was consumed)
            enrollment_file_id = None
            if 'enrollment_file' in locals():
                # EnrollmentFile record exists - update it to 'failed' instead of rolling back
                # This preserves the sequence ID (no gap)
                try:
                    enrollment_file.processing_status = 'failed'
                    enrollment_file.error_message = str(e)
                    self.db.commit()
                    enrollment_file_id = enrollment_file.enrollment_file_id
                except Exception:
                    self.db.rollback()
            else:
                # EnrollmentFile was not created yet - safe to rollback
                self.db.rollback()
            
            # Clean up JSON file if it was created but processing failed
            # This prevents orphaned JSON files from causing collision issues on retry
            if 'json_file_path' in locals() and json_file_path.exists():
                try:
                    json_file_path.unlink()
                except Exception as cleanup_error:
                    # Log cleanup failure but don't fail the error handling
                    pass
            
            # Log error (with enrollment_file_id if it exists)
            self._log_error(
                file_name=file_name,
                file_hash=file_hash,
                enrollment_file_id=enrollment_file_id,
                message=f"Processing exception: {str(e)}",
                error_code='PROCESSING_EXCEPTION',
                metadata={'exception_type': type(e).__name__}
            )
            
            # Commit error log
            try:
                self.db.commit()
            except Exception:
                self.db.rollback()
            
            return {
                'success': False,
                'enrollment_file_id': enrollment_file_id,  # Return ID if it was created (even if failed)
                'json_file_path': None,
                'error_message': f"Processing failed: {str(e)}"
            }
    
    def _check_duplicate(self, file_hash: str) -> Dict[str, Any]:
        """
        Check if a file with the same hash already exists.
        Only checks successfully processed files (processing_status='completed').
        
        Returns:
            Dict with duplicate check results:
            {
                'is_duplicate': bool,
                'message': str,
                'existing_file_id': Optional[int]
            }
        """
        # Only check successfully processed files for duplicates
        existing_file = self.db.query(EnrollmentFile).filter(
            EnrollmentFile.file_hash == file_hash,
            EnrollmentFile.client_id == self.client_id,
            EnrollmentFile.lob_id == self.lob_id,
            EnrollmentFile.processing_status == 'completed'  # Only successful files
        ).first()
        
        if existing_file:
            return {
                'is_duplicate': True,
                'message': f"File with same hash already exists (ID: {existing_file.enrollment_file_id})",
                'existing_file_id': existing_file.enrollment_file_id
            }
        
        return {
            'is_duplicate': False,
            'message': 'No duplicate found',
            'existing_file_id': None
        }
    
    
    def _log_error(
        self,
        file_name: str,
        file_hash: Optional[str],
        message: str,
        error_code: Optional[str] = None,
        enrollment_file_id: Optional[int] = None,
        segment_code: Optional[str] = None,
        element_ref: Optional[str] = None,
        line_number: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Log error to process_log table."""
        log_entry = ProcessLog(
                    enrollment_file_id=enrollment_file_id,
                    client_id=self.client_id,
                    lob_id=self.lob_id,
                    file_name=file_name,
                    file_hash=file_hash,
                    log_type='error',
                    log_level='ERROR',
                    message=message,
                    error_code=error_code,
                    segment_code=segment_code,
                    element_ref=element_ref,
                    line_number=line_number,
                    log_metadata=metadata
                )
        self.db.add(log_entry)
    
    def _log_warning(
        self,
        file_name: str,
        file_hash: Optional[str],
        message: str,
        error_code: Optional[str] = None,
        enrollment_file_id: Optional[int] = None,
        segment_code: Optional[str] = None,
        element_ref: Optional[str] = None,
        line_number: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Log warning to process_log table."""
        log_entry = ProcessLog(
            enrollment_file_id=enrollment_file_id,
            client_id=self.client_id,
            lob_id=self.lob_id,
            file_name=file_name,
            file_hash=file_hash,
            log_type='warning',
            log_level='WARN',
            message=message,
            error_code=error_code,
            segment_code=segment_code,
            element_ref=element_ref,
            line_number=line_number,
            log_metadata=metadata
        )
        self.db.add(log_entry)
    
    def _log_info(
        self,
        file_name: str,
        file_hash: Optional[str],
        message: str,
        error_code: Optional[str] = None,
        enrollment_file_id: Optional[int] = None,
        segment_code: Optional[str] = None,
        element_ref: Optional[str] = None,
        line_number: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Log info to process_log."""
        log_entry = ProcessLog(
            enrollment_file_id=enrollment_file_id,
            client_id=self.client_id,
            lob_id=self.lob_id,
            file_name=file_name,
            file_hash=file_hash,
            log_type='info',
            log_level='INFO',
            message=message,
            error_code=error_code,
            segment_code=segment_code,
            element_ref=element_ref,
            line_number=line_number,
            log_metadata=metadata
        )
        self.db.add(log_entry)
