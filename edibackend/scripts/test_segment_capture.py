"""
Test script to verify that the parser captures ALL segments correctly
Date: 2026-01-20
Purpose: Validate that JSON structure matches EDI structure exactly
"""
import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from app.services.treo_parser_834 import TreoParser834


def extract_edi_segments(edi_content: str) -> list:
    """Extract all segments from EDI content"""
    segments = []
    for line in edi_content.split('~'):
        if line.strip():
            seg_id = line.split('*')[0] if '*' in line else line[:10]
            segments.append({
                'segment_id': seg_id,
                'full_segment': line
            })
    return segments


def extract_json_segments(json_data: dict) -> list:
    """Extract all segments from JSON in sequence"""
    segments = []
    
    # Header segments
    if 'interchange' in json_data:
        inter = json_data['interchange']
        if 'isa' in inter:
            segments.append({'segment_id': 'ISA', 'source': 'header', 'data': inter['isa']})
    
    if 'functional_group' in json_data:
        fg = json_data['functional_group']
        if 'gs' in fg:
            segments.append({'segment_id': 'GS', 'source': 'header', 'data': fg['gs']})
    
    if 'transaction_set' in json_data:
        ts = json_data['transaction_set']
        if 'st' in ts:
            segments.append({'segment_id': 'ST', 'source': 'header', 'data': ts['st']})
        if 'bgn' in ts:
            segments.append({'segment_id': 'BGN', 'source': 'header', 'data': ts['bgn']})
        if 'ref' in ts:
            for ref in ts['ref']:
                segments.append({'segment_id': 'REF', 'source': 'header', 'data': ref})
        if 'dtp' in ts:
            for dtp in ts['dtp']:
                segments.append({'segment_id': 'DTP', 'source': 'header', 'data': dtp})
    
    # Member segments (loops)
    if 'loops' in json_data:
        for member_loop in json_data['loops']:
            member_segments = member_loop.get('segments', {})
            # Extract segments in order (we need to preserve order)
            # Since JSON dicts don't preserve order, we'll iterate through known segment types
            # But first, let's just collect all segments
            for seg_type, seg_list in member_segments.items():
                for seg_data in seg_list:
                    segments.append({
                        'segment_id': seg_type.upper(),
                        'source': 'member',
                        'data': seg_data
                    })
    
    # Trailer segments
    if 'transaction_set' in json_data:
        ts = json_data['transaction_set']
        if 'se' in ts:
            segments.append({'segment_id': 'SE', 'source': 'trailer', 'data': ts['se']})
    
    if 'functional_group' in json_data:
        fg = json_data['functional_group']
        if 'ge' in fg:
            segments.append({'segment_id': 'GE', 'source': 'trailer', 'data': fg['ge']})
    
    if 'interchange' in json_data:
        inter = json_data['interchange']
        if 'iea' in inter:
            segments.append({'segment_id': 'IEA', 'source': 'trailer', 'data': inter['iea']})
    
    return segments


def compare_member_segments(edi_member_segments: list, json_member_data: dict) -> dict:
    """Compare EDI member segments with JSON member data"""
    json_segments = json_member_data.get('segments', {})
    
    # Count segments in EDI
    edi_segment_counts = {}
    for seg in edi_member_segments:
        seg_id = seg['segment_id']
        edi_segment_counts[seg_id] = edi_segment_counts.get(seg_id, 0) + 1
    
    # Count segments in JSON
    json_segment_counts = {}
    for seg_type, seg_list in json_segments.items():
        json_segment_counts[seg_type.upper()] = len(seg_list)
    
    # Compare
    all_segment_types = set(edi_segment_counts.keys()) | set(json_segment_counts.keys())
    comparison = {}
    
    for seg_type in all_segment_types:
        edi_count = edi_segment_counts.get(seg_type, 0)
        json_count = json_segment_counts.get(seg_type, 0)
        comparison[seg_type] = {
            'edi_count': edi_count,
            'json_count': json_count,
            'match': edi_count == json_count
        }
    
    return comparison


def main():
    """Test segment capture"""
    print("=" * 80)
    print("Testing Segment Capture - Verifying JSON matches EDI structure")
    print("=" * 80)
    
    # Database session
    db = SessionLocalTreo()
    
    try:
        # Load EDI file
        edi_file_path = Path(__file__).parent.parent.parent / '1017_834.edi'
        
        if not edi_file_path.exists():
            print(f"ERROR: EDI file not found at {edi_file_path}")
            return 1
        
        print(f"\n1. Loading EDI file: {edi_file_path}")
        with open(edi_file_path, 'rb') as f:
            file_content = f.read()
        
        edi_content = file_content.decode('utf-8')
        edi_segments = extract_edi_segments(edi_content)
        
        print(f"   Total EDI segments: {len(edi_segments)}")
        
        # Find first member (INS segment)
        first_ins_index = None
        second_ins_index = None
        for i, seg in enumerate(edi_segments):
            if seg['segment_id'] == 'INS':
                if first_ins_index is None:
                    first_ins_index = i
                elif second_ins_index is None:
                    second_ins_index = i
                    break
        
        if first_ins_index is None:
            print("ERROR: No INS segment found in EDI file")
            return 1
        
        print(f"   First INS at segment index: {first_ins_index}")
        if second_ins_index:
            print(f"   Second INS at segment index: {second_ins_index}")
            first_member_edi_segments = edi_segments[first_ins_index:second_ins_index]
        else:
            # Only one member or last member
            first_member_edi_segments = edi_segments[first_ins_index:]
        
        print(f"   First member EDI segments: {len(first_member_edi_segments)}")
        print(f"   First member segment types: {[s['segment_id'] for s in first_member_edi_segments[:20]]}")
        
        # Process file with parser
        print(f"\n2. Processing EDI file with parser...")
        parser = TreoParser834(
            db=db,
            client_id=1,
            lob_id=6
        )
        
        result = parser.parse_and_store(
            file_name='1017_834.edi',
            file_content=file_content,
            created_by='test_segment_capture'
        )
        
        if not result.get('success'):
            print(f"❌ Processing FAILED: {result.get('error_message', 'Unknown error')}")
            return 1
        
        enrollment_file_id = result['enrollment_file_id']
        json_file_path = result.get('json_file_path')
        
        print(f"   ✅ Processing successful")
        print(f"   Enrollment File ID: {enrollment_file_id}")
        print(f"   JSON File Path: {json_file_path}")
        
        # Load JSON file
        if not json_file_path or not Path(json_file_path).exists():
            print(f"❌ JSON file not found: {json_file_path}")
            return 1
        
        print(f"\n3. Loading JSON file...")
        with open(json_file_path, 'r') as f:
            json_data = json.load(f)
        
        # Extract first member from JSON
        if 'loops' not in json_data or len(json_data['loops']) == 0:
            print("❌ No loops found in JSON")
            return 1
        
        first_member_json = json_data['loops'][0]
        
        print(f"   First member loop_id: {first_member_json.get('loop_id')}")
        print(f"   First member segments: {list(first_member_json.get('segments', {}).keys())}")
        
        # Compare segment counts
        print(f"\n4. Comparing EDI vs JSON segment counts for first member...")
        print("-" * 80)
        
        comparison = compare_member_segments(first_member_edi_segments, first_member_json)
        
        all_match = True
        for seg_type, counts in sorted(comparison.items()):
            match_symbol = "✅" if counts['match'] else "❌"
            print(f"{match_symbol} {seg_type:5s}: EDI={counts['edi_count']:3d}, JSON={counts['json_count']:3d}")
            if not counts['match']:
                all_match = False
        
        print("-" * 80)
        
        # Show detailed segment list for first member
        print(f"\n5. First member EDI segment sequence (first 30):")
        print("-" * 80)
        for i, seg in enumerate(first_member_edi_segments[:30]):
            seg_preview = seg['full_segment'][:60] + "..." if len(seg['full_segment']) > 60 else seg['full_segment']
            print(f"{i+1:3d}. {seg['segment_id']:5s}: {seg_preview}")
        
        # Show JSON segments for first member
        print(f"\n6. First member JSON segments summary:")
        print("-" * 80)
        json_segments = first_member_json.get('segments', {})
        for seg_type, seg_list in sorted(json_segments.items()):
            print(f"   {seg_type.upper():5s}: {len(seg_list)} instance(s)")
            if len(seg_list) > 0 and len(seg_list) <= 3:
                # Show sample data for small lists
                for j, seg_data in enumerate(seg_list):
                    first_key = list(seg_data.keys())[0] if seg_data else 'N/A'
                    first_val = str(seg_data.get(first_key, ''))[:40] if seg_data else ''
                    print(f"      [{j+1}] {first_key}={first_val}")
        
        # Summary
        print(f"\n" + "=" * 80)
        print("VALIDATION SUMMARY")
        print("=" * 80)
        
        if all_match:
            print("✅ All segment counts match between EDI and JSON")
        else:
            print("❌ Some segment counts do not match")
            print("   This indicates the parser may be missing some segments")
        
        total_edi_segments = len(first_member_edi_segments)
        total_json_segments = sum(len(seg_list) for seg_list in json_segments.values())
        
        print(f"\n   Total EDI segments in first member: {total_edi_segments}")
        print(f"   Total JSON segments in first member: {total_json_segments}")
        
        if total_edi_segments == total_json_segments:
            print("   ✅ Total segment count matches")
        else:
            print(f"   ❌ Total segment count mismatch: {total_edi_segments} vs {total_json_segments}")
        
        return 0 if all_match and total_edi_segments == total_json_segments else 1
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
        
    finally:
        db.close()


if __name__ == '__main__':
    sys.exit(main())
