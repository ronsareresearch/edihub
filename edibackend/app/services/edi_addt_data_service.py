"""
[TREO] - EDI Additional Data Service
Date: 2026-01-21

Purpose:
    Service to populate edi_addt_data table from parsed EDI JSON data.
    Extracts Additional Reporting Categories data from LS/LE loops (Loop 2700).

Structure:
    - LS Segment: 1 instance, 1 element (Loop Start)
    - LX Segment: 1 instance, 1 element (Transaction Set Line Number)
    - N1 Segment: 1 instance, 2 elements (Name/Entity Information)
    - REF Segment: 1 instance, 2 elements (Reference Information)
    - DTP Segment: 1 instance, 3 elements (Date/Time/Period)
    - LE Segment: 1 instance, 1 element (Loop End)
"""
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.models.treo_models import EDIAddtData


class EDIAddtDataService:
    """
    Service to populate edi_addt_data table from parsed EDI JSON data.
    Extracts Additional Reporting Categories data from LS/LE loops (Loop 2700).
    """

    @staticmethod
    def populate_from_json(
        db_session: Session,
        enrollment_file_id: int,
        json_data: Dict[str, Any]
    ) -> List[EDIAddtData]:
        """
        Populate edi_addt_data table from parsed JSON data.
        Extracts LS/LE loops from member records and creates one row per LS/LE loop.

        Args:
            db_session: Database session
            enrollment_file_id: Enrollment file ID
            json_data: Parsed EDI JSON structure containing loops array

        Returns:
            List of EDIAddtData instances
        """
        loops = json_data.get('loops', [])
        edi_addt_data_records = []
        
        # Track ls_le_index globally per ref02_1 across all member occurrences
        # This ensures unique composite keys when the same member appears in multiple transaction sets
        ref02_1_ls_le_index_map = {}
        
        for member_loop in loops:
            segments = member_loop.get('segments', {})
            
            # Get ref02_1 from the first REF segment (subscriber identifier)
            ref_list = segments.get('ref', [])
            ref02_1 = None
            for ref in ref_list:
                if ref.get('ref01') == '0F':  # Subscriber identifier
                    ref02_1 = ref.get('ref02')
                    break
            
            if not ref02_1:
                # Skip if no subscriber identifier found
                continue
            
            # Initialize ls_le_index counter for this ref02_1 if not already present
            if ref02_1 not in ref02_1_ls_le_index_map:
                ref02_1_ls_le_index_map[ref02_1] = 0
            
            # Extract LS/LE loops from member_loop
            # The parser now captures LS/LE loops as nested structures in 'ls_le_loops'
            ls_le_loops = member_loop.get('ls_le_loops', [])
            
            for ls_le_loop in ls_le_loops:
                # Increment global ls_le_index for this ref02_1
                ref02_1_ls_le_index_map[ref02_1] += 1
                ls_le_index = ref02_1_ls_le_index_map[ref02_1]
                # Extract segments from LS/LE loop
                ls = ls_le_loop.get('ls', {})
                le = ls_le_loop.get('le', {})
                loop_segments = ls_le_loop.get('segments', {})
                
                # Extract segments within the LS/LE loop
                lx_list = loop_segments.get('lx', [])
                n1_list = loop_segments.get('n1', [])
                ref_list_loop = loop_segments.get('ref', [])
                dtp_list_loop = loop_segments.get('dtp', [])
                
                # Get the first instance of each segment type
                lx = lx_list[0] if lx_list else {}
                n1 = n1_list[0] if n1_list else {}
                ref_in_loop = ref_list_loop[0] if ref_list_loop else {}
                dtp = dtp_list_loop[0] if dtp_list_loop else {}
                
                # Create EDIAddtData record
                edi_addt_data = EDIAddtData(
                    enrollment_file_id=enrollment_file_id,
                    ref02_1=ref02_1,
                    ls_le_index=ls_le_index,
                    
                    # LS Segment
                    ls01=ls.get('ls01'),
                    
                    # LX Segment
                    lx01=lx.get('lx01'),
                    
                    # N1 Segment
                    n101=n1.get('n101'),
                    n102=n1.get('n102'),
                    
                    # REF Segment
                    ref01=ref_in_loop.get('ref01'),
                    ref02=ref_in_loop.get('ref02'),
                    
                    # DTP Segment
                    dtp01=dtp.get('dtp01'),
                    dtp02=dtp.get('dtp02'),
                    dtp03=dtp.get('dtp03'),
                    
                    # LE Segment
                    le01=le.get('le01'),
                )
                
                edi_addt_data_records.append(edi_addt_data)
                db_session.add(edi_addt_data)
        
        return edi_addt_data_records
