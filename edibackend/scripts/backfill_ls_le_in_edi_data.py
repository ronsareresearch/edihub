"""
Script to backfill ls01 and le01 values in edi_data table from JSON file.
This fixes the issue where LS/LE segments were not being populated in edi_data.
"""
import sys
from pathlib import Path
import json
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from sqlalchemy import text

def backfill_ls_le(enrollment_file_id: int):
    """
    Backfill ls01 and le01 values in edi_data table from JSON file.
    
    Args:
        enrollment_file_id: Enrollment file ID to process
    """
    db = SessionLocalTreo()
    
    try:
        # Get file info to find JSON file
        result = db.execute(
            text("""
                SELECT file_name, original_file_path
                FROM public.enrollment_files
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        file_info = result.fetchone()
        
        if not file_info:
            print(f"❌ Enrollment file {enrollment_file_id} not found")
            return
        
        file_name = file_info[0]
        original_file_path = file_info[1]
        
        # Construct JSON file path
        if original_file_path:
            # original_file_path is like "data/json_files/{file_name}"
            json_file_path = Path(__file__).parent.parent / original_file_path
        else:
            # Fallback: try to find JSON file by enrollment_file_id
            json_files_dir = Path(__file__).parent.parent / 'data' / 'json_files'
            # Try common naming patterns
            possible_names = [
                f"{file_name.replace('.edi', '').replace('.x12', '').replace('.txt', '')}.json",
                f"{file_name.replace('.edi', '').replace('.x12', '').replace('.txt', '')}_1.json",
            ]
            json_file_path = None
            for name in possible_names:
                candidate = json_files_dir / name
                if candidate.exists():
                    json_file_path = candidate
                    break
            
            if not json_file_path:
                print(f"❌ Could not find JSON file for enrollment_file_id {enrollment_file_id}")
                print(f"   Tried: {[str(json_files_dir / n) for n in possible_names]}")
                return
        
        if not json_file_path.exists():
            print(f"❌ JSON file not found: {json_file_path}")
            return
        
        print(f"📂 Loading JSON file: {json_file_path}")
        
        # Load JSON data
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        loops = json_data.get('loops', [])
        print(f"📊 Found {len(loops):,} member loops in JSON")
        
        # Process each member loop
        updates = []
        for member_index, member_loop in enumerate(loops, start=1):
            ls_le_loops = member_loop.get('ls_le_loops', [])
            
            if ls_le_loops:
                # Get ls01 from first LS segment
                first_ls_loop = ls_le_loops[0]
                ls01_value = None
                if 'ls' in first_ls_loop and first_ls_loop['ls']:
                    ls01_value = first_ls_loop['ls'].get('ls01')
                
                # Get le01 from last LE segment
                last_ls_loop = ls_le_loops[-1]
                le01_value = None
                if 'le' in last_ls_loop and last_ls_loop['le']:
                    le01_value = last_ls_loop['le'].get('le01')
                
                if ls01_value or le01_value:
                    updates.append({
                        'member_index': member_index,
                        'ls01': ls01_value,
                        'le01': le01_value
                    })
        
        print(f"📝 Found {len(updates):,} members with LS/LE data to update")
        
        # Update database
        updated_count = 0
        for update in updates:
            db.execute(
                text("""
                    UPDATE public.edi_data
                    SET ls01 = :ls01, le01 = :le01
                    WHERE enrollment_file_id = :file_id AND member_index = :member_index
                """),
                {
                    'file_id': enrollment_file_id,
                    'member_index': update['member_index'],
                    'ls01': update['ls01'],
                    'le01': update['le01']
                }
            )
            updated_count += 1
        
        # Commit changes
        db.commit()
        
        print(f"✅ Successfully updated {updated_count:,} records")
        
        # Verify update
        result = db.execute(
            text("""
                SELECT 
                    COUNT(*) as total_records,
                    COUNT(ls01) as ls01_populated,
                    COUNT(le01) as le01_populated,
                    COUNT(CASE WHEN ls01 IS NOT NULL AND le01 IS NOT NULL THEN 1 END) as both_populated
                FROM public.edi_data
                WHERE enrollment_file_id = :file_id
            """),
            {'file_id': enrollment_file_id}
        )
        stats = result.fetchone()
        
        print(f"\n📊 Verification:")
        print(f"   Total records: {stats[0]:,}")
        print(f"   ls01 populated: {stats[1]:,}")
        print(f"   le01 populated: {stats[2]:,}")
        print(f"   Both populated: {stats[3]:,}")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python backfill_ls_le_in_edi_data.py <enrollment_file_id>")
        print("Example: python backfill_ls_le_in_edi_data.py 2")
        sys.exit(1)
    
    enrollment_file_id = int(sys.argv[1])
    backfill_ls_le(enrollment_file_id)
