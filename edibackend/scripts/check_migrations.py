"""Check current migration status"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import engine
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text('SELECT version_num FROM alembic_version'))
    row = result.fetchone()
    if row:
        print(f"Current migration version in database: {row[0]}")
    else:
        print("No migration version found in database")
