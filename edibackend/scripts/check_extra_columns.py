"""Check if extra columns have data"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Check REF 13-14
    result = conn.execute(text("""
        SELECT 
            COUNT(*) as total,
            COUNT(ref01_13) as ref13_count,
            COUNT(ref01_14) as ref14_count
        FROM public.edi_data
    """))
    row = result.fetchone()
    print(f"Total records: {row[0]}")
    print(f"Records with ref01_13: {row[1]}")
    print(f"Records with ref01_14: {row[2]}")
    
    # Check DTP 11-24
    result = conn.execute(text("""
        SELECT 
            COUNT(dtp01_11) as dtp11_count,
            COUNT(dtp01_12) as dtp12_count,
            COUNT(dtp01_13) as dtp13_count,
            COUNT(dtp01_20) as dtp20_count,
            COUNT(dtp01_24) as dtp24_count
        FROM public.edi_data
    """))
    row = result.fetchone()
    print(f"\nDTP column usage:")
    print(f"  dtp01_11: {row[0]} records")
    print(f"  dtp01_12: {row[1]} records")
    print(f"  dtp01_13: {row[2]} records")
    print(f"  dtp01_20: {row[3]} records")
    print(f"  dtp01_24: {row[4]} records")
