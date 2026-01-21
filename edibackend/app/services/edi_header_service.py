"""
[TREO] - EDI Header Service
Date: 2026-01-20
Purpose: Populate edi_header table from parsed EDI JSON data
"""
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.treo_models import EDIHeader


class EDIHeaderService:
    """
    Service to populate edi_header table from parsed EDI JSON data.
    Flattens EDI header segments (ISA, GS, ST, BGN, REF, DTP, QTY, SE, GE, IEA) into columns.
    """
    
    @staticmethod
    def populate_from_json(
        db_session: Session,
        enrollment_file_id: int,
        json_data: Dict[str, Any]
    ) -> EDIHeader:
        """
        Populate edi_header table from parsed JSON data.
        
        Args:
            db_session: Database session
            enrollment_file_id: Enrollment file ID (primary key)
            json_data: Parsed EDI JSON structure containing interchange, functional_group, transaction_set
            
        Returns:
            EDIHeader instance
        """
        interchange = json_data.get('interchange', {})
        functional_group = json_data.get('functional_group', {})
        transaction_set = json_data.get('transaction_set', {})
        
        # Extract ISA segment
        isa = interchange.get('isa', {})
        
        # Extract IEA segment
        iea = interchange.get('iea', {})
        
        # Extract GS segment
        gs = functional_group.get('gs', {})
        
        # Extract GE segment
        ge = functional_group.get('ge', {})
        
        # Extract ST segment
        st = transaction_set.get('st', {})
        
        # Extract BGN segment
        bgn = transaction_set.get('bgn', {})
        
        # Extract REF segments (array, first instance only)
        ref_list = transaction_set.get('ref', [])
        ref_first = ref_list[0] if ref_list else {}
        
        # Extract DTP segments (array, up to 2 instances)
        dtp_list = transaction_set.get('dtp', [])
        dtp_first = dtp_list[0] if len(dtp_list) > 0 else {}
        dtp_second = dtp_list[1] if len(dtp_list) > 1 else {}
        
        # Extract SE segment
        se = transaction_set.get('se', {})
        
        # Create EDIHeader record
        edi_header = EDIHeader(
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
            
            # ST Segment (3 elements)
            st01=st.get('st01'),
            st02=st.get('st02'),
            st03=st.get('st03'),
            
            # BGN Segment (8 elements)
            bgn01=bgn.get('bgn01'),
            bgn02=bgn.get('bgn02'),
            bgn03=bgn.get('bgn03'),
            bgn04=bgn.get('bgn04'),
            bgn05=bgn.get('bgn05'),
            bgn06=bgn.get('bgn06'),
            bgn07=bgn.get('bgn07'),
            bgn08=bgn.get('bgn08'),
            
            # REF Segment - 1 instance (2 elements, simplified)
            ref01=ref_first.get('ref01'),
            ref02=ref_first.get('ref02'),
            
            # DTP Segment - 2 instances (3 elements each)
            dtp01_1=dtp_first.get('dtp01'),
            dtp02_1=dtp_first.get('dtp02'),
            dtp03_1=dtp_first.get('dtp03'),
            dtp01_2=dtp_second.get('dtp01'),
            dtp02_2=dtp_second.get('dtp02'),
            dtp03_2=dtp_second.get('dtp03'),
            
            # SE Segment (2 elements)
            se01=se.get('se01'),
            se02=se.get('se02'),
            
            # GE Segment (2 elements)
            ge01=ge.get('ge01'),
            ge02=ge.get('ge02'),
            
            # IEA Segment (2 elements)
            iea01=iea.get('iea01'),
            iea02=iea.get('iea02'),
        )
        
        db_session.add(edi_header)
        return edi_header
