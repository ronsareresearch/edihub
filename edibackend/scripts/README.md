# Database Seeding Scripts

This directory contains scripts for seeding initial data into the database.

## Available Scripts

### `seed_virginia_medicaid.py`

Seeds the Virginia Medicaid client and associated Line of Business (LOB) records based on the EDI 834 Companion Guide.

**Usage:**
```bash
cd edibackend
uv run python scripts/seed_virginia_medicaid.py
```

**What it creates:**
- **Client**: Commonwealth of Virginia - Department of Medical Assistance Services (DMAS)
  - Client Code: `VA_MEDICAID`
  
- **Line of Businesses (7 total)**:
  1. **MCO** - Managed Care Organizations (MCOs)
  2. **MMP** - Medicare-Medicaid Plans (MMPs)
  3. **BEHAVIORAL_HEALTH** - Behavioral Health Service Provider
  4. **DENTAL** - Dental Service Provider
  5. **TRANSPORTATION** - Transportation Service Provider (NEMT Broker)
  6. **CCC_PLUS** - CCC Plus Plans
  7. **MEDALLION_4** - Medallion 4.0 Plans

**Features:**
- Idempotent - can be run multiple times safely
- Checks for existing records before creating
- Updates existing records if they already exist
- All LOBs are set to `is_active = True`
- All program types are set to `MEDICAID`

**Based on:**
- EDI 834 Companion Guide Version 2.8 (September 14, 2022)
- Commonwealth of Virginia, Department of Medical Assistance Services (DMAS)
- Document: `EDI_834_Companion_Guide.md`
