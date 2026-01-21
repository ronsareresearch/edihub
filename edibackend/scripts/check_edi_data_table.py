"""Check edi_data table structure and data"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Check if table exists
    result = conn.execute(text("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'edi_data'
        )
    """))
    table_exists = result.fetchone()[0]
    print(f"edi_data table exists: {table_exists}")
    
    if table_exists:
        # Count records
        result = conn.execute(text("SELECT COUNT(*) FROM public.edi_data"))
        count = result.fetchone()[0]
        print(f"Current edi_data records: {count}")
        
        # Check columns
        result = conn.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_schema = 'public' 
            AND table_name = 'edi_data'
            ORDER BY ordinal_position
        """))
        columns = [row[0] for row in result.fetchall()]
        print(f"\nTotal columns: {len(columns)}")
        
        # Check for REF and DTP columns
        ref_columns = [c for c in columns if c.startswith('ref')]
        dtp_columns = [c for c in columns if c.startswith('dtp')]
        
        print(f"\nREF columns: {len(ref_columns)}")
        ref_instances = set()
        for col in ref_columns:
            if '_' in col:
                instance = col.split('_')[1]
                ref_instances.add(instance)
        print(f"  REF instances: {sorted(ref_instances)}")
        
        print(f"\nDTP columns: {len(dtp_columns)}")
        dtp_instances = set()
        for col in dtp_columns:
            if '_' in col:
                instance = col.split('_')[1]
                dtp_instances.add(instance)
        print(f"  DTP instances: {sorted(dtp_instances)}")
