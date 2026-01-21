"""
[TREO] - EDI Control Segments Service
Date: 2026-01-21
Purpose: Populate edi_control_seg table from parsed EDI JSON data
"""
from typing import Dict, Any
from sqlalchemy.orm import Session
from app.models.treo_models import EDIControlSeg


class EDIControlSegService:
    """
    Service to populate edi_control_seg table from parsed EDI JSON data.
    Flattens file-level control segments (ISA, GS, GE, IEA) into columns.
    """
    
    @staticmethod
    def populate_from_json(
        db_session: Session,
        enrollment_file_id: int,
        json_data: Dict[str, Any]
    ) -> EDIControlSeg:
        """
        Populate edi_control_seg table from parsed JSON data.
        
        Args:
            db_session: Database session
            enrollment_file_id: Enrollment file ID (primary key)
            json_data: Parsed EDI JSON structure containing interchange, functional_group
            
        Returns:
            EDIControlSeg instance
        """
        interchange = json_data.get('interchange', {})
        functional_group = json_data.get('functional_group', {})
        
        # Extract ISA segment
        isa = interchange.get('isa', {})
        
        # Extract IEA segment
        iea = interchange.get('iea', {})
        
        # Extract GS segment
        gs = functional_group.get('gs', {})
        
        # Extract GE segment
        ge = functional_group.get('ge', {})
        
        # Create EDIControlSeg record
        edi_control_seg = EDIControlSeg(
            enrollment_file_id=enrollment_file_id,
            
            # ISA Segment (16 elements)
            isa01=isa.get('isa01'),
            isa02=isa.get('isa02'),
            isa03=isa.get('isa03'),
            isa04=isa.get('isa04'),
            isa05=isa.get('isa05'),
            isa06=isa.get('isa06'),
            isa07=isa.get('isa07'),
            isa08=isa.get('isa08'),
            isa09=isa.get('isa09'),
            isa10=isa.get('isa10'),
            isa11=isa.get('isa11'),
            isa12=isa.get('isa12'),
            isa13=isa.get('isa13'),
            isa14=isa.get('isa14'),
            isa15=isa.get('isa15'),
            isa16=isa.get('isa16'),
            
            # GS Segment (8 elements)
            gs01=gs.get('gs01'),
            gs02=gs.get('gs02'),
            gs03=gs.get('gs03'),
            gs04=gs.get('gs04'),
            gs05=gs.get('gs05'),
            gs06=gs.get('gs06'),
            gs07=gs.get('gs07'),
            gs08=gs.get('gs08'),
            
            # GE Segment (2 elements)
            ge01=ge.get('ge01'),
            ge02=ge.get('ge02'),
            
            # IEA Segment (2 elements)
            iea01=iea.get('iea01'),
            iea02=iea.get('iea02'),
        )
        
        db_session.add(edi_control_seg)
        return edi_control_seg
