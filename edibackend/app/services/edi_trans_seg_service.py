"""
[TREO] - EDI Transaction Segments Service
Date: 2026-01-21
Purpose: Populate edi_trans_seg table from parsed EDI JSON data
"""
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.models.treo_models import EDITransSeg


class EDITransSegService:
    """
    Service to populate edi_trans_seg table from parsed EDI JSON data.
    Flattens transaction-level segments (ST, BGN, REF, DTP, N1, SE) into columns.
    Creates one row per transaction set (ST/SE pair).
    """
    
    @staticmethod
    def populate_from_json(
        db_session: Session,
        enrollment_file_id: int,
        json_data: Dict[str, Any]
    ) -> List[EDITransSeg]:
        """
        Populate edi_trans_seg table from parsed JSON data.
        Creates one row per transaction set (ST/SE pair).
        
        Args:
            db_session: Database session
            enrollment_file_id: Enrollment file ID
            json_data: Parsed EDI JSON structure containing transaction_set
            
        Returns:
            List of EDITransSeg instances
        """
        transaction_set = json_data.get('transaction_set', {})
        
        # Get ST segments (array - multiple transaction sets)
        st_list = transaction_set.get('st', [])
        
        # Get SE segments (array - multiple transaction sets)
        se_list = transaction_set.get('se', [])
        
        # Get BGN segments (array - one per transaction set)
        bgn_list = transaction_set.get('bgn', [])
        if not isinstance(bgn_list, list):
            bgn_list = [bgn_list] if bgn_list else []
        
        # Get REF segments (array of arrays - one array per transaction set)
        ref_list = transaction_set.get('ref', [])
        if not isinstance(ref_list, list):
            ref_list = [ref_list] if ref_list else []
        
        # Get DTP segments (array of arrays - one array per transaction set)
        dtp_list = transaction_set.get('dtp', [])
        if not isinstance(dtp_list, list):
            dtp_list = [dtp_list] if dtp_list else []
        
        # Get N1 segments (array of arrays - one array per transaction set)
        n1_list = transaction_set.get('n1', [])
        if not isinstance(n1_list, list):
            n1_list = [n1_list] if n1_list else []
        
        edi_trans_seg_records = []
        
        # Determine number of transaction sets
        # Use the maximum of ST count, SE count, BGN count, or 1 (if no arrays, assume single transaction)
        num_transactions = max(
            len(st_list) if isinstance(st_list, list) and st_list else 0,
            len(se_list) if isinstance(se_list, list) and se_list else 0,
            len(bgn_list) if bgn_list else 0,
            1  # Default to 1 if no arrays
        )
        
        # For each transaction set, create a record
        for trans_index in range(1, num_transactions + 1):
            trans_array_index = trans_index - 1  # 0-based array index
            
            # Get ST segment for this transaction
            st = st_list[trans_array_index] if isinstance(st_list, list) and len(st_list) > trans_array_index else (st_list if isinstance(st_list, dict) else {})
            
            # Get SE segment for this transaction
            se = se_list[trans_array_index] if isinstance(se_list, list) and len(se_list) > trans_array_index else (se_list if isinstance(se_list, dict) else {})
            
            # Get BGN segment for this transaction
            bgn = bgn_list[trans_array_index] if len(bgn_list) > trans_array_index else (bgn_list[0] if bgn_list and isinstance(bgn_list[0], dict) else {})
            
            # Get REF segments for this transaction (array of REF instances for this transaction)
            ref_instances = []
            if len(ref_list) > trans_array_index:
                ref_trans = ref_list[trans_array_index]
                if isinstance(ref_trans, list):
                    ref_instances = ref_trans[:5]  # Limit to 5 instances
                elif isinstance(ref_trans, dict):
                    ref_instances = [ref_trans]
            elif len(ref_list) > 0:
                # Fallback: use first transaction's REF if this transaction doesn't have any
                ref_trans = ref_list[0]
                if isinstance(ref_trans, list):
                    ref_instances = ref_trans[:5]
                elif isinstance(ref_trans, dict):
                    ref_instances = [ref_trans]
            
            # Get DTP segments for this transaction
            dtp_instances = []
            if len(dtp_list) > trans_array_index:
                dtp_trans = dtp_list[trans_array_index]
                if isinstance(dtp_trans, list):
                    dtp_instances = dtp_trans[:5]  # Limit to 5 instances
                elif isinstance(dtp_trans, dict):
                    dtp_instances = [dtp_trans]
            elif len(dtp_list) > 0:
                # Fallback: use first transaction's DTP if this transaction doesn't have any
                dtp_trans = dtp_list[0]
                if isinstance(dtp_trans, list):
                    dtp_instances = dtp_trans[:5]
                elif isinstance(dtp_trans, dict):
                    dtp_instances = [dtp_trans]
            
            # Get N1 segments for this transaction
            n1_instances = []
            if len(n1_list) > trans_array_index:
                n1_trans = n1_list[trans_array_index]
                if isinstance(n1_trans, list):
                    n1_instances = n1_trans[:3]  # Limit to 3 instances
                elif isinstance(n1_trans, dict):
                    n1_instances = [n1_trans]
            elif len(n1_list) > 0:
                # Fallback: use first transaction's N1 if this transaction doesn't have any
                n1_trans = n1_list[0]
                if isinstance(n1_trans, list):
                    n1_instances = n1_trans[:3]
                elif isinstance(n1_trans, dict):
                    n1_instances = [n1_trans]
            
            # Create EDITransSeg record
            edi_trans_seg = EDITransSeg(
                enrollment_file_id=enrollment_file_id,
                trans_index=trans_index,
                
                # ST Segment (3 elements)
                st01=st.get('st01') if isinstance(st, dict) else None,
                st02=st.get('st02') if isinstance(st, dict) else None,
                st03=st.get('st03') if isinstance(st, dict) else None,
                
                # BGN Segment (8 elements) - use for first transaction only
                bgn01=bgn.get('bgn01') if trans_index == 1 else None,
                bgn02=bgn.get('bgn02') if trans_index == 1 else None,
                bgn03=bgn.get('bgn03') if trans_index == 1 else None,
                bgn04=bgn.get('bgn04') if trans_index == 1 else None,
                bgn05=bgn.get('bgn05') if trans_index == 1 else None,
                bgn06=bgn.get('bgn06') if trans_index == 1 else None,
                bgn07=bgn.get('bgn07') if trans_index == 1 else None,
                bgn08=bgn.get('bgn08') if trans_index == 1 else None,
                
                # REF Segments (up to 5 instances, 2 elements each)
                ref01_1=ref_instances[0].get('ref01') if len(ref_instances) > 0 else None,
                ref02_1=ref_instances[0].get('ref02') if len(ref_instances) > 0 else None,
                ref01_2=ref_instances[1].get('ref01') if len(ref_instances) > 1 else None,
                ref02_2=ref_instances[1].get('ref02') if len(ref_instances) > 1 else None,
                ref01_3=ref_instances[2].get('ref01') if len(ref_instances) > 2 else None,
                ref02_3=ref_instances[2].get('ref02') if len(ref_instances) > 2 else None,
                ref01_4=ref_instances[3].get('ref01') if len(ref_instances) > 3 else None,
                ref02_4=ref_instances[3].get('ref02') if len(ref_instances) > 3 else None,
                ref01_5=ref_instances[4].get('ref01') if len(ref_instances) > 4 else None,
                ref02_5=ref_instances[4].get('ref02') if len(ref_instances) > 4 else None,
                
                # DTP Segments (up to 5 instances, 3 elements each)
                dtp01_1=dtp_instances[0].get('dtp01') if len(dtp_instances) > 0 else None,
                dtp02_1=dtp_instances[0].get('dtp02') if len(dtp_instances) > 0 else None,
                dtp03_1=dtp_instances[0].get('dtp03') if len(dtp_instances) > 0 else None,
                dtp01_2=dtp_instances[1].get('dtp01') if len(dtp_instances) > 1 else None,
                dtp02_2=dtp_instances[1].get('dtp02') if len(dtp_instances) > 1 else None,
                dtp03_2=dtp_instances[1].get('dtp03') if len(dtp_instances) > 1 else None,
                dtp01_3=dtp_instances[2].get('dtp01') if len(dtp_instances) > 2 else None,
                dtp02_3=dtp_instances[2].get('dtp02') if len(dtp_instances) > 2 else None,
                dtp03_3=dtp_instances[2].get('dtp03') if len(dtp_instances) > 2 else None,
                dtp01_4=dtp_instances[3].get('dtp01') if len(dtp_instances) > 3 else None,
                dtp02_4=dtp_instances[3].get('dtp02') if len(dtp_instances) > 3 else None,
                dtp03_4=dtp_instances[3].get('dtp03') if len(dtp_instances) > 3 else None,
                dtp01_5=dtp_instances[4].get('dtp01') if len(dtp_instances) > 4 else None,
                dtp02_5=dtp_instances[4].get('dtp02') if len(dtp_instances) > 4 else None,
                dtp03_5=dtp_instances[4].get('dtp03') if len(dtp_instances) > 4 else None,
                
                # N1 Segments (up to 3 instances, 2 elements each)
                n101_1=n1_instances[0].get('n101') if len(n1_instances) > 0 else None,
                n102_1=n1_instances[0].get('n102') if len(n1_instances) > 0 else None,
                n101_2=n1_instances[1].get('n101') if len(n1_instances) > 1 else None,
                n102_2=n1_instances[1].get('n102') if len(n1_instances) > 1 else None,
                n101_3=n1_instances[2].get('n101') if len(n1_instances) > 2 else None,
                n102_3=n1_instances[2].get('n102') if len(n1_instances) > 2 else None,
                
                # SE Segment (2 elements)
                se01=se.get('se01') if isinstance(se, dict) else None,
                se02=se.get('se02') if isinstance(se, dict) else None,
            )
            
            db_session.add(edi_trans_seg)
            edi_trans_seg_records.append(edi_trans_seg)
        
        return edi_trans_seg_records
