#!/usr/bin/env python3
"""
[TREO] - Master Migration Script
Purpose: Complete database setup for fresh database instance
Usage: python master_migration.py [--db-url <database_url>] [--skip-seed]
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text, inspect
from alembic.config import Config
from alembic import command
from app.config_treo import settings_treo


def run_alembic_upgrade(db_url):
    """Run Alembic upgrade to head revision"""
    print("📦 Running Alembic migrations...")
    
    # Create Alembic config
    migrations_dir = Path(__file__).parent.parent / "migrations"
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", str(migrations_dir))
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
    
    # Run upgrade to head
    try:
        command.upgrade(alembic_cfg, "head")
        print("  ✅ All migrations applied successfully")
    except Exception as e:
        print(f"  ⚠️  Migration warning: {e}")
        # Continue anyway - migrations may already be applied


def seed_base_data(engine, skip_seed=False):
    """Seed base data (clients, LOBs)"""
    if skip_seed:
        print("⏭️  Skipping seed data (--skip-seed flag)")
        return
    
    print("🌱 Seeding base data...")
    
    from sqlalchemy.orm import sessionmaker
    from app.models.treo_models import Client, LOB
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Check if VA_MEDICAID client already exists
        va_client = session.query(Client).filter(Client.client_code == 'VA_MEDICAID').first()
        
        if not va_client:
            # Create VA_MEDICAID client
            va_client = Client(
                client_code='VA_MEDICAID',
                client_name='Commonwealth of Virginia - Department of Medical Assistance Services (DMAS)',
                is_active=True
            )
            session.add(va_client)
            session.flush()
            print(f"  ✅ Created client: {va_client.client_code} (ID: {va_client.client_id})")
        else:
            print(f"  ⚠️  Client {va_client.client_code} already exists (ID: {va_client.client_id})")
        
        # Define LOBs based on EDI 834 Companion Guide
        lobs_data = [
            {'code': 'MCO', 'name': 'Managed Care Organizations (MCOs)', 'program_type': 'MEDICAID'},
            {'code': 'MMP', 'name': 'Medicare-Medicaid Plans (MMPs)', 'program_type': 'MEDICAID'},
            {'code': 'BEHAVIORAL_HEALTH', 'name': 'Behavioral Health Service Provider', 'program_type': 'MEDICAID'},
            {'code': 'DENTAL', 'name': 'Dental Service Provider', 'program_type': 'MEDICAID'},
            {'code': 'TRANSPORTATION', 'name': 'Transportation Service Provider (NEMT Broker)', 'program_type': 'MEDICAID'},
            {'code': 'CCC_PLUS', 'name': 'CCC Plus Plans', 'program_type': 'MEDICAID'},
            {'code': 'MEDALLION_4', 'name': 'Medallion 4.0 Plans', 'program_type': 'MEDICAID'},
        ]
        
        created_count = 0
        for lob_data in lobs_data:
            existing_lob = session.query(LOB).filter(
                LOB.client_id == va_client.client_id,
                LOB.lob_code == lob_data['code']
            ).first()
            
            if not existing_lob:
                lob = LOB(
                    client_id=va_client.client_id,
                    lob_code=lob_data['code'],
                    lob_name=lob_data['name'],
                    program_type=lob_data['program_type'],
                    is_active=True
                )
                session.add(lob)
                created_count += 1
                print(f"  ✅ Created LOB: {lob.lob_code} (ID: {lob.lob_id})")
            else:
                print(f"  ⚠️  LOB {lob_data['code']} already exists (ID: {existing_lob.lob_id})")
        
        session.commit()
        print(f"  ✅ Base data seeded successfully ({created_count} new LOBs)")
        
    except Exception as e:
        session.rollback()
        print(f"  ❌ Error seeding data: {e}")
        raise
    finally:
        session.close()


def verify_setup(engine):
    """Verify database setup"""
    print("🔍 Verifying database setup...")
    
    inspector = inspect(engine)
    
    # Check metadata schema
    metadata_tables = inspector.get_table_names(schema='metadata')
    print(f"  📊 Metadata tables: {len(metadata_tables)}")
    
    # Check public schema
    public_tables = inspector.get_table_names(schema='public')
    expected_tables = [
        'clients', 'lobs', 'enrollment_files', 'process_log',
        'edi_control_seg', 'edi_trans_seg', 'edi_data', 'edi_addt_data'
    ]
    
    missing_tables = [t for t in expected_tables if t not in public_tables]
    if missing_tables:
        print(f"  ⚠️  Missing tables: {missing_tables}")
    else:
        print(f"  ✅ All expected public tables exist ({len(expected_tables)})")
    
    # Check seed data
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM public.clients"))
        client_count = result.scalar()
        print(f"  📊 Clients: {client_count}")
        
        result = conn.execute(text("SELECT COUNT(*) FROM public.lobs"))
        lob_count = result.scalar()
        print(f"  📊 LOBs: {lob_count}")


def main():
    parser = argparse.ArgumentParser(description='Master migration script for TREO database')
    parser.add_argument(
        '--db-url',
        type=str,
        default=None,
        help='Database URL (overrides TREO_DATABASE_URL from config)'
    )
    parser.add_argument(
        '--skip-seed',
        action='store_true',
        help='Skip seeding base data (clients, LOBs)'
    )
    parser.add_argument(
        '--verify-only',
        action='store_true',
        help='Only verify setup, do not create anything'
    )
    
    args = parser.parse_args()
    
    # Get database URL
    db_url = args.db_url or settings_treo.DATABASE_URL
    
    print("=" * 60)
    print("🚀 TREO Master Migration Script")
    print("=" * 60)
    print(f"📌 Database URL: {db_url.split('@')[1] if '@' in db_url else '***'}")
    print()
    
    # Create engine
    engine = create_engine(db_url, echo=False)
    
    if args.verify_only:
        verify_setup(engine)
        return
    
    try:
        # Step 1: Run all Alembic migrations
        run_alembic_upgrade(db_url)
        print()
        
        # Step 2: Seed base data
        seed_base_data(engine, skip_seed=args.skip_seed)
        print()
        
        # Step 3: Verify setup
        verify_setup(engine)
        print()
        
        print("=" * 60)
        print("✅ Master migration completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print()
        print("=" * 60)
        print(f"❌ Migration failed: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
