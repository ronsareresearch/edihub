"""
[TREO] - JSON File Name Generator
Date: 2026-01-20
Purpose: Flexible JSON file naming with template support and dynamic placeholders

Features:
- Template-based naming patterns
- Dynamic placeholders (file_id, hash, timestamp, client_id, lob_id, etc.)
- Client/LOB-specific configurations
- Collision detection and handling
- Validation and sanitization
"""
from typing import Dict, Optional, Any
from sqlalchemy.orm import Session
from datetime import datetime
from pathlib import Path
import re


class JSONFileNameGenerator:
    """
    Flexible JSON file naming generator with template support.
    
    Features:
    - Template-based naming patterns
    - Dynamic placeholders (file_id, hash, timestamp, etc.)
    - Client/LOB-specific naming rules
    - Collision detection and auto-increment
    - File name sanitization
    """
    
    # Default naming pattern
    DEFAULT_PATTERN = "{file_name_stem}.json"
    
    # Available placeholders
    AVAILABLE_PLACEHOLDERS = [
        'file_name_stem',      # Original file name without extension
        'file_name',           # Original file name with extension
        'file_id',             # enrollment_file_id (when available)
        'file_hash',           # Full SHA-256 hash
        'file_hash_8',         # First 8 characters of hash
        'file_hash_16',        # First 16 characters of hash
        'timestamp',           # YYYYMMDD_HHMMSS format
        'date',                # YYYYMMDD format
        'time',                # HHMMSS format
        'client_id',           # Client ID
        'lob_id',              # LOB ID
        'client_code',         # Client code (from Client table)
        'lob_code',            # LOB code (from LOB table)
    ]
    
    def __init__(
        self,
        naming_pattern: Optional[str] = None,
        client_id: Optional[int] = None,
        lob_id: Optional[int] = None,
        db_session: Optional[Session] = None,
        json_files_dir: Optional[Path] = None
    ):
        """
        Initialize file name generator.
        
        Args:
            naming_pattern: Template pattern (default: "{file_name_stem}.json")
            client_id: Client ID for placeholders
            lob_id: LOB ID for placeholders
            db_session: Optional database session for client/LOB lookups
            json_files_dir: Directory where JSON files are stored (for collision detection)
        """
        self.naming_pattern = naming_pattern or self.DEFAULT_PATTERN
        self.client_id = client_id
        self.lob_id = lob_id
        self.db_session = db_session
        self.json_files_dir = json_files_dir
        
        # Cache for client/LOB codes
        self._client_code_cache: Optional[str] = None
        self._lob_code_cache: Optional[str] = None
        
        # Validate pattern
        self._validate_pattern()
    
    def _validate_pattern(self):
        """Validate that all placeholders in pattern are available."""
        placeholders = re.findall(r'\{([^}]+)\}', self.naming_pattern)
        invalid = [p for p in placeholders if p not in self.AVAILABLE_PLACEHOLDERS]
        if invalid:
            raise ValueError(
                f"Invalid placeholders in pattern: {invalid}. "
                f"Available: {self.AVAILABLE_PLACEHOLDERS}"
            )
    
    def _get_client_code(self) -> Optional[str]:
        """Get client code from database."""
        if self._client_code_cache is not None:
            return self._client_code_cache
        
        if not self.db_session or not self.client_id:
            return None
        
        try:
            from app.models.treo_models import Client
            client = self.db_session.query(Client).filter(
                Client.client_id == self.client_id
            ).first()
            
            if client:
                self._client_code_cache = client.client_code
                return client.client_code
        except Exception:
            pass
        
        return None
    
    def _get_lob_code(self) -> Optional[str]:
        """Get LOB code from database."""
        if self._lob_code_cache is not None:
            return self._lob_code_cache
        
        if not self.db_session or not self.lob_id:
            return None
        
        try:
            from app.models.treo_models import LOB
            lob = self.db_session.query(LOB).filter(
                LOB.lob_id == self.lob_id
            ).first()
            
            if lob:
                self._lob_code_cache = lob.lob_code
                return lob.lob_code
        except Exception:
            pass
        
        return None
    
    def _sanitize_filename(self, filename: str) -> str:
        """
        Sanitize filename by removing/replacing unsafe characters.
        
        Args:
            filename: Raw filename
            
        Returns:
            Sanitized filename safe for filesystem
        """
        # Remove or replace unsafe characters
        unsafe_chars = r'[<>:"/\\|?*\x00-\x1f]'
        sanitized = re.sub(unsafe_chars, '_', filename)
        
        # Remove leading/trailing dots and spaces
        sanitized = sanitized.strip('. ')
        
        # Limit length (keep reasonable, filesystems have limits)
        if len(sanitized) > 200:
            sanitized = sanitized[:200]
        
        return sanitized
    
    def _get_placeholder_value(self, placeholder: str, context: Dict[str, Any]) -> str:
        """Get value for a placeholder from context."""
        if placeholder == 'file_name_stem':
            file_name = context.get('original_file_name', '')
            return Path(file_name).stem
        
        if placeholder == 'file_name':
            return context.get('original_file_name', '')
        
        if placeholder == 'file_id':
            file_id = context.get('file_id')
            return str(file_id) if file_id is not None else ''
        
        if placeholder == 'file_hash':
            return context.get('file_hash', '')
        
        if placeholder == 'file_hash_8':
            file_hash = context.get('file_hash', '')
            return file_hash[:8] if len(file_hash) >= 8 else file_hash
        
        if placeholder == 'file_hash_16':
            file_hash = context.get('file_hash', '')
            return file_hash[:16] if len(file_hash) >= 16 else file_hash
        
        if placeholder == 'timestamp':
            return datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        
        if placeholder == 'date':
            return datetime.utcnow().strftime('%Y%m%d')
        
        if placeholder == 'time':
            return datetime.utcnow().strftime('%H%M%S')
        
        if placeholder == 'client_id':
            return str(self.client_id) if self.client_id else ''
        
        if placeholder == 'lob_id':
            return str(self.lob_id) if self.lob_id else ''
        
        if placeholder == 'client_code':
            client_code = self._get_client_code()
            return client_code if client_code else ''
        
        if placeholder == 'lob_code':
            lob_code = self._get_lob_code()
            return lob_code if lob_code else ''
        
        return ''
    
    def _check_file_exists(self, file_name: str) -> bool:
        """Check if file already exists."""
        if not self.json_files_dir:
            return False
        
        file_path = self.json_files_dir / file_name
        return file_path.exists()
    
    def _generate_with_collision_handling(
        self,
        base_file_name: str,
        ensure_unique: bool
    ) -> str:
        """
        Generate filename with collision handling.
        
        Args:
            base_file_name: Base filename to use
            ensure_unique: If True, auto-increment on collision
            
        Returns:
            Final filename (may be modified if collision detected)
        """
        if not ensure_unique or not self._check_file_exists(base_file_name):
            return base_file_name
        
        # Auto-increment: add _1, _2, _3, etc.
        name_part = Path(base_file_name).stem
        extension = Path(base_file_name).suffix
        
        counter = 1
        while True:
            new_name = f"{name_part}_{counter}{extension}"
            if not self._check_file_exists(new_name):
                return new_name
            counter += 1
            
            # Safety limit
            if counter > 10000:
                raise ValueError(f"Too many collisions for filename: {base_file_name}")
    
    def generate(
        self,
        original_file_name: str,
        file_hash: str,
        file_id: Optional[int] = None,
        ensure_unique: bool = True,
        check_existing: bool = True
    ) -> Dict[str, str]:
        """
        Generate JSON file name based on pattern.
        
        Args:
            original_file_name: Original EDI file name
            file_hash: SHA-256 hash of file
            file_id: Optional enrollment_file_id (for placeholders)
            ensure_unique: If True, handle collisions with auto-increment
            check_existing: If True, check if file exists (requires json_files_dir)
            
        Returns:
            {
                'file_name': 'generated_file_name.json',
                'relative_path': 'data/json_files/generated_file_name.json',
                'absolute_path': '/full/path/to/file.json' (if json_files_dir provided)
            }
        """
        # Build context for placeholders
        context = {
            'original_file_name': original_file_name,
            'file_hash': file_hash,
            'file_id': file_id
        }
        
        # Replace placeholders in pattern
        file_name = self.naming_pattern
        placeholders = re.findall(r'\{([^}]+)\}', file_name)
        
        for placeholder in placeholders:
            value = self._get_placeholder_value(placeholder, context)
            # Replace placeholder with value
            file_name = file_name.replace(f'{{{placeholder}}}', value)
        
        # Sanitize filename
        file_name = self._sanitize_filename(file_name)
        
        # Ensure .json extension
        if not file_name.endswith('.json'):
            file_name = f"{file_name}.json"
        
        # Handle collisions if needed
        if ensure_unique and check_existing:
            file_name = self._generate_with_collision_handling(file_name, ensure_unique)
        
        # Build paths
        relative_path = f"data/json_files/{file_name}"
        
        result = {
            'file_name': file_name,
            'relative_path': relative_path
        }
        
        if self.json_files_dir:
            absolute_path = str(self.json_files_dir / file_name)
            result['absolute_path'] = absolute_path
        
        return result
