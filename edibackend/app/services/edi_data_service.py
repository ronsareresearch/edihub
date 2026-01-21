"""
[TREO] - EDI Data Service
Date: 2026-01-20

Purpose:
    Service to populate edi_data table from parsed EDI JSON data.
    Flattens EDI member-level data (Loop 2000) into columns.

Complete structure based on parsed JSON:
    - INS Segment: 1 instance, 8 elements
    - REF Segment: Up to 12 instances, 2 elements each (max 11 found in data, +1 safety margin)
    - DTP Segment: Up to 10 instances, 3 elements each (max 9 found in data, +1 safety margin)
    - NM1 Segment: 1 instance, 4 elements
    - N3 Segment: 1 instance, 2 elements
    - N4 Segment: 1 instance, 6 elements
    - DMG Segment: 1 instance, 5 elements
    - LUI Segment: 1 instance, 2 elements
    - HD Segment: Up to 2 instances, 4 elements each
    - AMT Segment: 1 instance, 2 elements
    - LS Segment: 1 instance, 1 element (Additional Reporting Categories)
    - LE Segment: 1 instance, 1 element (Additional Reporting Categories Loop Termination)
"""
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.models.treo_models import EDIData


class EDIDataService:
    """
    Service to populate edi_data table from parsed EDI JSON data.
    Flattens EDI member-level data (Loop 2000) into columns.
    """

    @staticmethod
    def populate_from_json(
        db_session: Session,
        enrollment_file_id: int,
        json_data: Dict[str, Any]
    ) -> List[EDIData]:
        """
        Populate edi_data table from parsed JSON data.
        Each member (Loop 2000) becomes one row.

        Args:
            db_session: Database session
            enrollment_file_id: Enrollment file ID
            json_data: Parsed EDI JSON structure containing loops array

        Returns:
            List of EDIData instances
        """
        loops = json_data.get('loops', [])
        edi_data_records = []
        
        for member_index, member_loop in enumerate(loops, start=1):
            # Extract segments from member loop
            segments = member_loop.get('segments', {})
            
            # Extract INS segment
            ins_list = segments.get('ins', [])
            ins = ins_list[0] if ins_list else {}
            
            # Extract REF segments (array, up to 12 instances)
            ref_list = segments.get('ref', [])
            
            # Extract DTP segments (array, up to 10 instances)
            dtp_list = segments.get('dtp', [])
            
            # Extract NM1 segment (Name/Entity Information)
            nm1_list = segments.get('nm1', [])
            nm1 = nm1_list[0] if nm1_list else {}
            
            # Extract N3 segment (Address Information)
            n3_list = segments.get('n3', [])
            n3 = n3_list[0] if n3_list else {}
            
            # Extract N4 segment (Geographic Location)
            n4_list = segments.get('n4', [])
            n4 = n4_list[0] if n4_list else {}
            
            # Extract DMG segment (Demographic Information)
            dmg_list = segments.get('dmg', [])
            dmg = dmg_list[0] if dmg_list else {}
            
            # Extract LUI segment (Language)
            lui_list = segments.get('lui', [])
            lui = lui_list[0] if lui_list else {}
            
            # Extract HD segments (Health Coverage) - Up to 2 instances
            hd_list = segments.get('hd', [])
            
            # Extract AMT segment (Monetary Amount)
            amt_list = segments.get('amt', [])
            amt = amt_list[0] if amt_list else {}
            
            # Extract LS/LE segments from ls_le_loops array
            # The parser stores LS/LE loops in a separate array, not in segments
            ls_le_loops = member_loop.get('ls_le_loops', [])
            ls01_value = None
            le01_value = None
            
            if ls_le_loops:
                # Get ls01 from the first LS segment in the first ls_le_loop
                first_ls_loop = ls_le_loops[0]
                if 'ls' in first_ls_loop and first_ls_loop['ls']:
                    ls01_value = first_ls_loop['ls'].get('ls01')
                
                # Get le01 from the last LE segment in the last ls_le_loop
                last_ls_loop = ls_le_loops[-1]
                if 'le' in last_ls_loop and last_ls_loop['le']:
                    le01_value = last_ls_loop['le'].get('le01')
            
            # Create EDIData record
            edi_data = EDIData(
                enrollment_file_id=enrollment_file_id,
                member_index=member_index,
                
                # INS Segment (8 elements)
                ins01=ins.get('ins01'),
                ins02=ins.get('ins02'),
                ins03=ins.get('ins03'),
                ins04=ins.get('ins04'),
                ins05=ins.get('ins05'),
                ins06=ins.get('ins06'),
                ins07=ins.get('ins07'),
                ins08=ins.get('ins08'),
                
                # REF Segment - Up to 12 instances (2 elements each)
                ref01_1=ref_list[0].get('ref01') if len(ref_list) > 0 else None,
                ref02_1=ref_list[0].get('ref02') if len(ref_list) > 0 else None,
                ref01_2=ref_list[1].get('ref01') if len(ref_list) > 1 else None,
                ref02_2=ref_list[1].get('ref02') if len(ref_list) > 1 else None,
                ref01_3=ref_list[2].get('ref01') if len(ref_list) > 2 else None,
                ref02_3=ref_list[2].get('ref02') if len(ref_list) > 2 else None,
                ref01_4=ref_list[3].get('ref01') if len(ref_list) > 3 else None,
                ref02_4=ref_list[3].get('ref02') if len(ref_list) > 3 else None,
                ref01_5=ref_list[4].get('ref01') if len(ref_list) > 4 else None,
                ref02_5=ref_list[4].get('ref02') if len(ref_list) > 4 else None,
                ref01_6=ref_list[5].get('ref01') if len(ref_list) > 5 else None,
                ref02_6=ref_list[5].get('ref02') if len(ref_list) > 5 else None,
                ref01_7=ref_list[6].get('ref01') if len(ref_list) > 6 else None,
                ref02_7=ref_list[6].get('ref02') if len(ref_list) > 6 else None,
                ref01_8=ref_list[7].get('ref01') if len(ref_list) > 7 else None,
                ref02_8=ref_list[7].get('ref02') if len(ref_list) > 7 else None,
                ref01_9=ref_list[8].get('ref01') if len(ref_list) > 8 else None,
                ref02_9=ref_list[8].get('ref02') if len(ref_list) > 8 else None,
                ref01_10=ref_list[9].get('ref01') if len(ref_list) > 9 else None,
                ref02_10=ref_list[9].get('ref02') if len(ref_list) > 9 else None,
                ref01_11=ref_list[10].get('ref01') if len(ref_list) > 10 else None,
                ref02_11=ref_list[10].get('ref02') if len(ref_list) > 10 else None,
                ref01_12=ref_list[11].get('ref01') if len(ref_list) > 11 else None,
                ref02_12=ref_list[11].get('ref02') if len(ref_list) > 11 else None,
                
                # DTP Segment - Up to 10 instances (3 elements each)
                dtp01_1=dtp_list[0].get('dtp01') if len(dtp_list) > 0 else None,
                dtp02_1=dtp_list[0].get('dtp02') if len(dtp_list) > 0 else None,
                dtp03_1=dtp_list[0].get('dtp03') if len(dtp_list) > 0 else None,
                dtp01_2=dtp_list[1].get('dtp01') if len(dtp_list) > 1 else None,
                dtp02_2=dtp_list[1].get('dtp02') if len(dtp_list) > 1 else None,
                dtp03_2=dtp_list[1].get('dtp03') if len(dtp_list) > 1 else None,
                dtp01_3=dtp_list[2].get('dtp01') if len(dtp_list) > 2 else None,
                dtp02_3=dtp_list[2].get('dtp02') if len(dtp_list) > 2 else None,
                dtp03_3=dtp_list[2].get('dtp03') if len(dtp_list) > 2 else None,
                dtp01_4=dtp_list[3].get('dtp01') if len(dtp_list) > 3 else None,
                dtp02_4=dtp_list[3].get('dtp02') if len(dtp_list) > 3 else None,
                dtp03_4=dtp_list[3].get('dtp03') if len(dtp_list) > 3 else None,
                dtp01_5=dtp_list[4].get('dtp01') if len(dtp_list) > 4 else None,
                dtp02_5=dtp_list[4].get('dtp02') if len(dtp_list) > 4 else None,
                dtp03_5=dtp_list[4].get('dtp03') if len(dtp_list) > 4 else None,
                dtp01_6=dtp_list[5].get('dtp01') if len(dtp_list) > 5 else None,
                dtp02_6=dtp_list[5].get('dtp02') if len(dtp_list) > 5 else None,
                dtp03_6=dtp_list[5].get('dtp03') if len(dtp_list) > 5 else None,
                dtp01_7=dtp_list[6].get('dtp01') if len(dtp_list) > 6 else None,
                dtp02_7=dtp_list[6].get('dtp02') if len(dtp_list) > 6 else None,
                dtp03_7=dtp_list[6].get('dtp03') if len(dtp_list) > 6 else None,
                dtp01_8=dtp_list[7].get('dtp01') if len(dtp_list) > 7 else None,
                dtp02_8=dtp_list[7].get('dtp02') if len(dtp_list) > 7 else None,
                dtp03_8=dtp_list[7].get('dtp03') if len(dtp_list) > 7 else None,
                dtp01_9=dtp_list[8].get('dtp01') if len(dtp_list) > 8 else None,
                dtp02_9=dtp_list[8].get('dtp02') if len(dtp_list) > 8 else None,
                dtp03_9=dtp_list[8].get('dtp03') if len(dtp_list) > 8 else None,
                dtp01_10=dtp_list[9].get('dtp01') if len(dtp_list) > 9 else None,
                dtp02_10=dtp_list[9].get('dtp02') if len(dtp_list) > 9 else None,
                dtp03_10=dtp_list[9].get('dtp03') if len(dtp_list) > 9 else None,
                
                # NM1 Segment (Name/Entity Information) - 1 instance, 4 elements
                nm101=nm1.get('nm101'),
                nm102=nm1.get('nm102'),
                nm103=nm1.get('nm103'),
                nm104=nm1.get('nm104'),
                
                # N3 Segment (Address Information) - 1 instance, 2 elements
                n301=n3.get('n301'),
                n302=n3.get('n302'),
                
                # N4 Segment (Geographic Location) - 1 instance, 6 elements
                n401=n4.get('n401'),
                n402=n4.get('n402'),
                n403=n4.get('n403'),
                n404=n4.get('n404'),
                n405=n4.get('n405'),
                n406=n4.get('n406'),
                
                # DMG Segment (Demographic Information) - 1 instance, 5 elements
                dmg01=dmg.get('dmg01'),
                dmg02=dmg.get('dmg02'),
                dmg03=dmg.get('dmg03'),
                dmg04=dmg.get('dmg04'),
                dmg05=dmg.get('dmg05'),
                
                # LUI Segment (Language) - 1 instance, 2 elements
                lui01=lui.get('lui01'),
                lui02=lui.get('lui02'),
                
                # HD Segment (Health Coverage) - Up to 2 instances, 4 elements each
                hd01_1=hd_list[0].get('hd01') if len(hd_list) > 0 else None,
                hd02_1=hd_list[0].get('hd02') if len(hd_list) > 0 else None,
                hd03_1=hd_list[0].get('hd03') if len(hd_list) > 0 else None,
                hd04_1=hd_list[0].get('hd04') if len(hd_list) > 0 else None,
                hd01_2=hd_list[1].get('hd01') if len(hd_list) > 1 else None,
                hd02_2=hd_list[1].get('hd02') if len(hd_list) > 1 else None,
                hd03_2=hd_list[1].get('hd03') if len(hd_list) > 1 else None,
                hd04_2=hd_list[1].get('hd04') if len(hd_list) > 1 else None,
                
                # AMT Segment (Monetary Amount) - 1 instance, 2 elements
                amt01=amt.get('amt01'),
                amt02=amt.get('amt02'),
                
                # LS Segment (Additional Reporting Categories) - 1 instance, 1 element
                # Extracted from ls_le_loops array (first LS segment)
                ls01=ls01_value,
                
                # LE Segment (Additional Reporting Categories Loop Termination) - 1 instance, 1 element
                # Extracted from ls_le_loops array (last LE segment)
                le01=le01_value,
            )
            
            edi_data_records.append(edi_data)
            db_session.add(edi_data)
        
        return edi_data_records
