# Master Migration Script

## Overview

The `master_migration.py` script provides a complete database setup for a fresh TREO database instance. It runs all Alembic migrations and seeds base data (clients and LOBs).

## Usage

### Basic Usage

Run the script with default database URL from config:

```bash
cd edibackend
uv run python scripts/master_migration.py
```

### Custom Database URL

Override the database URL:

```bash
uv run python scripts/master_migration.py --db-url "postgresql://user:password@host:5432/dbname"
```

### Skip Seed Data

Skip seeding base data (useful if you only want to run migrations):

```bash
uv run python scripts/master_migration.py --skip-seed
```

### Verify Only

Check the current state of the database without making changes:

```bash
uv run python scripts/master_migration.py --verify-only
```

## What It Does

1. **Runs All Alembic Migrations**
   - Creates `metadata` schema and all metadata tables
   - Creates `public` schema tables:
     - `clients`
     - `lobs`
     - `enrollment_files`
     - `process_log`
   - Creates EDI data tables:
     - `edi_control_seg`
     - `edi_trans_seg`
     - `edi_data`
     - `edi_addt_data`

2. **Seeds Base Data**
   - Creates `VA_MEDICAID` client
   - Creates LOBs for Virginia Medicaid:
     - MCO (Managed Care Organizations)
     - MMP (Medicare-Medicaid Plans)
     - BEHAVIORAL_HEALTH
     - DENTAL
     - TRANSPORTATION
     - CCC_PLUS
     - MEDALLION_4

3. **Verifies Setup**
   - Checks that all expected tables exist
   - Verifies seed data was created

## Configuration

The script uses the database URL from `app.config_treo.settings_treo.DATABASE_URL` by default. You can override it using the `--db-url` parameter.

To configure the default database URL, set the `TREO_DATABASE_URL` environment variable or update `edibackend/app/config_treo.py`.

## Idempotency

The script is designed to be idempotent:
- Alembic migrations will only apply new migrations that haven't been run
- Seed data checks for existing records before creating new ones
- Safe to run multiple times

## Requirements

- Python 3.8+
- All project dependencies installed (`uv install` or `pip install -r requirements.txt`)
- PostgreSQL database server running
- Database user with CREATE TABLE and INSERT permissions

## Example Output

```
============================================================
🚀 TREO Master Migration Script
============================================================
📌 Database URL: localhost:5432/enroll

📦 Running Alembic migrations...
  ✅ All migrations applied successfully

🌱 Seeding base data...
  ✅ Created client: VA_MEDICAID (ID: 1)
  ✅ Created LOB: MCO (ID: 1)
  ✅ Created LOB: MMP (ID: 2)
  ...
  ✅ Base data seeded successfully (7 new LOBs)

🔍 Verifying database setup...
  📊 Metadata tables: 15
  ✅ All expected public tables exist (8)
  📊 Clients: 1
  📊 LOBs: 7

============================================================
✅ Master migration completed successfully!
============================================================
```
