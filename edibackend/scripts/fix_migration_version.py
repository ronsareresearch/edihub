"""Fix migration version in database"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import engine
from sqlalchemy import text

# Check if edi_header table exists
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'edi_header'
        )
    """))
    edi_header_exists = result.fetchone()[0]
    print(f"edi_header table exists: {edi_header_exists}")
    
    # Check if edi_data table exists
    result = conn.execute(text("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'edi_data'
        )
    """))
    edi_data_exists = result.fetchone()[0]
    print(f"edi_data table exists: {edi_data_exists}")
    
    # Update migration version
    if edi_header_exists and not edi_data_exists:
        # We're at 007ca0eee656, need to go to 008db1e2f789
        conn.execute(text("UPDATE alembic_version SET version_num = '007ca0eee656'"))
        conn.commit()
        print("Updated migration version to 007ca0eee656")
    elif edi_header_exists and edi_data_exists:
        # Both exist, update to latest
        conn.execute(text("UPDATE alembic_version SET version_num = '008db1e2f789'"))
        conn.commit()
        print("Updated migration version to 008db1e2f789")
    else:
        # Need to go back further
        conn.execute(text("UPDATE alembic_version SET version_num = 'f48e7c708003'"))
        conn.commit()
        print("Updated migration version to f48e7c708003")
