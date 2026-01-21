"""
[TREO] - EDI 834 Metadata Loader (Database-Driven)
Date: 2026-01-20
Purpose: Load all EDI 834 metadata from database into in-memory structures for fast parsing

Features:
- Loads all loops, segments, elements from database
- Builds qualifier-based loop detection maps
- Creates fast lookup indices for parsing
- Supports config file overrides for client customizations
"""
from typing import Dict, List, Optional, Any, Tuple
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy import select
from app.models.treo_metadata import (
    Loop, Segment, Element, LoopSegment, LoopElement,
    CodeValue, IndustryUsage, ElementDataType
)


class MetadataLoader834:
    """
    Loads EDI 834 metadata from database into in-memory structures.
    
    All parsing metadata comes from database tables. Config files can
    optionally override specific settings for client customizations.
    """
    
    def __init__(self, db_session: Session, config_overrides: Optional[Dict[str, Any]] = None):
        """
        Initialize metadata loader.
        
        Args:
            db_session: SQLAlchemy database session
            config_overrides: Optional config file overrides for client customizations
        """
        self.db = db_session
        self.config_overrides = config_overrides or {}
        
        # In-memory metadata structures
        self.loops: Dict[str, Dict[str, Any]] = {}
        self.segments: Dict[str, Dict[str, Any]] = {}
        self.elements: Dict[int, Dict[str, Any]] = {}
        
        # Fast lookup indices
        self.qualifier_to_loop: Dict[Tuple[str, str, str], str] = {}  # (segment, element, qualifier) -> loop_id
        self.segment_to_loops: Dict[str, List[str]] = {}  # segment_code -> [loop_ids]
        self.loop_segment_sequence: Dict[str, List[Dict[str, Any]]] = {}  # loop_id -> [segment_defs]
        self.initiating_segments: Dict[str, str] = {}  # loop_id -> initiating_segment_code
        
    def load_all(self) -> Dict[str, Any]:
        """
        Load all metadata from database into in-memory structures.
        
        Returns:
            Unified metadata dictionary with all parsing information
        """
        # Load core metadata
        self._load_loops()
        self._load_segments()
        self._load_elements()
        self._load_loop_segments()
        self._load_code_values()
        
        # Build lookup indices
        self._build_lookup_indices()
        
        # Build segment sequences
        self._build_segment_sequences()
        
        # Apply config overrides if provided
        if self.config_overrides:
            self._apply_config_overrides()
        
        return {
            'loops': self.loops,
            'segments': self.segments,
            'elements': self.elements,
            'qualifier_to_loop': self.qualifier_to_loop,
            'segment_to_loops': self.segment_to_loops,
            'loop_segment_sequence': self.loop_segment_sequence,
            'initiating_segments': self.initiating_segments
        }
    
    def _load_loops(self):
        """Load all loops from database (optimized - simple query)"""
        db_loops = self.db.query(Loop).order_by(Loop.loopid).all()
        
        for loop in db_loops:
            loop_id_lower = loop.loopid.lower()
            self.loops[loop_id_lower] = {
                'loop_id': loop.loop_id,
                'loopid': loop.loopid,
                'name': loop.name,
                'repeat_min': loop.repeat_min,
                'repeat_max': loop.repeat_max,
                'loop_desc': loop.loop_desc,
                'segments': [],
                'nested_loops': []
            }
    
    def _load_segments(self):
        """Load all segments from database (optimized - simple query)"""
        db_segments = self.db.query(Segment).all()
        
        for segment in db_segments:
            self.segments[segment.segmentid] = {
                'segment_id': segment.segment_id,
                'segmentid': segment.segmentid,
                'elements': []
            }
    
    def _load_elements(self):
        """Load all elements from database with segments (optimized with eager loading)"""
        # Load elements with their segments to avoid N+1 queries later
        db_elements = (
            self.db.query(Element)
            .options(joinedload(Element.segment))
            .all()
        )
        
        for element in db_elements:
            self.elements[element.element_id] = {
                'element_id': element.element_id,
                'segment_id': element.segment_id,
                'ref_designator': element.ref_designator,
                'name': element.name,
                'min_length': element.min_length,
                'max_length': element.max_length,
                'parent_element_id': element.parent_element_id,
                'segment': element.segment  # Store segment reference for code_values
            }
    
    def _load_loop_segments(self):
        """Load loop-segment relationships and build segment sequences (optimized with eager loading)"""
        # Get all loop-segment relationships with eager loading to avoid N+1 queries
        db_loop_segments = (
            self.db.query(LoopSegment)
            .options(
                joinedload(LoopSegment.loop),
                joinedload(LoopSegment.segment),
                joinedload(LoopSegment.usage)
            )
            .order_by(LoopSegment.loop_id, LoopSegment.order_no)
            .all()
        )
        
        for ls in db_loop_segments:
            loop_id_lower = ls.loop.loopid.lower()
            segment_code = ls.segment.segmentid
            
            segment_def = {
                'segment_id': ls.segment_id,
                'segment_code': segment_code,
                'segment_name': ls.segment_name,
                'order_no': ls.order_no,
                'usage_type': ls.usage.usage_type,  # R, S, O, etc.
                'repeat_min': ls.segment_repeat_min,
                'repeat_max': ls.segment_repeat_max,
                'loop_id': ls.loop_id
            }
            
            # Add to loop's segment list
            if loop_id_lower in self.loops:
                self.loops[loop_id_lower]['segments'].append(segment_def)
                
                # Track which segments belong to which loops
                if segment_code not in self.segment_to_loops:
                    self.segment_to_loops[segment_code] = []
                if loop_id_lower not in self.segment_to_loops[segment_code]:
                    self.segment_to_loops[segment_code].append(loop_id_lower)
    
    def _load_code_values(self):
        """Load code values for qualifier-based loop detection (optimized with eager loading)"""
        # Preload segments to avoid N+1 queries when accessing element.segment
        # First, load all elements with their segments
        elements_map = {
            e.element_id: e for e in 
            self.db.query(Element).options(joinedload(Element.segment)).all()
        }
        
        # Get all code values with eager loading for loops
        db_code_values = (
            self.db.query(CodeValue)
            .options(joinedload(CodeValue.loop))
            .all()
        )
        
        for cv in db_code_values:
            # Get element from preloaded map
            element = elements_map.get(cv.element_id)
            if not element or not element.segment:
                continue
                
            segment_code = element.segment.segmentid
            element_ref = element.ref_designator
            qualifier_value = cv.value
            loop_id_lower = cv.loop.loopid.lower() if cv.loop else None
            
            if not loop_id_lower:
                continue  # Skip invalid entries
            
            # Build qualifier lookup: (segment, element, qualifier) -> loop_id
            key = (segment_code, element_ref, qualifier_value)
            self.qualifier_to_loop[key] = loop_id_lower
    
    def _build_lookup_indices(self):
        """Build fast lookup indices for parsing"""
        # Find initiating segments for each loop
        # Initiating segment is the first segment in a loop
        for loop_id_lower, loop_data in self.loops.items():
            if loop_data['segments']:
                first_segment = loop_data['segments'][0]
                initiating_seg = first_segment['segment_code']
                self.initiating_segments[loop_id_lower] = initiating_seg
    
    def _build_segment_sequences(self):
        """Build segment sequence for each loop"""
        for loop_id_lower, loop_data in self.loops.items():
            # Segments are already in order_no order from _load_loop_segments
            self.loop_segment_sequence[loop_id_lower] = loop_data['segments']
    
    def _apply_config_overrides(self):
        """
        Apply config file overrides for client customizations.
        
        This allows config files to override database metadata for:
        - Custom loop sequences
        - Custom exit conditions
        - Client-specific segment handling
        """
        # Example override structure:
        # config_overrides = {
        #     'loops': {
        #         '1000a': {
        #             'exit_conditions': [...],
        #             'custom_segment_order': [...]
        #         }
        #     }
        # }
        
        if 'loops' in self.config_overrides:
            for loop_id, overrides in self.config_overrides['loops'].items():
                loop_id_lower = loop_id.lower()
                if loop_id_lower in self.loops:
                    # Merge overrides into loop data
                    self.loops[loop_id_lower].update(overrides)
    
    def get_loop_by_qualifier(self, segment_code: str, element_ref: str, qualifier_value: str) -> Optional[str]:
        """
        Get loop ID by qualifier (for qualifier-based loop detection).
        
        Args:
            segment_code: Segment code (e.g., 'N1')
            element_ref: Element reference (e.g., 'N101')
            qualifier_value: Qualifier value (e.g., 'P5', 'IN')
            
        Returns:
            Loop ID if found, None otherwise
        """
        key = (segment_code, element_ref, qualifier_value)
        return self.qualifier_to_loop.get(key)
    
    def get_loop_segments(self, loop_id: str) -> List[Dict[str, Any]]:
        """
        Get segments for a loop in order.
        
        Args:
            loop_id: Loop ID (e.g., '1000a', '2000')
            
        Returns:
            List of segment definitions in order
        """
        loop_id_lower = loop_id.lower()
        return self.loop_segment_sequence.get(loop_id_lower, [])
    
    def get_initiating_segment(self, loop_id: str) -> Optional[str]:
        """
        Get initiating segment for a loop.
        
        Args:
            loop_id: Loop ID (e.g., '1000a', '2000')
            
        Returns:
            Initiating segment code, or None if not found
        """
        loop_id_lower = loop_id.lower()
        return self.initiating_segments.get(loop_id_lower)
    
    def is_valid_segment_in_loop(self, segment_code: str, loop_id: str) -> bool:
        """
        Check if a segment belongs to a loop.
        
        Args:
            segment_code: Segment code (e.g., 'N1', 'INS')
            loop_id: Loop ID (e.g., '1000a', '2000')
            
        Returns:
            True if segment belongs to loop, False otherwise
        """
        loop_id_lower = loop_id.lower()
        loop_segments = self.get_loop_segments(loop_id_lower)
        return any(seg['segment_code'] == segment_code for seg in loop_segments)
