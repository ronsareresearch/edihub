"""
Seed Virginia Medicaid Client and LOBs
Date: 2026-01-20
Purpose: Create initial client and Line of Business records based on EDI 834 Companion Guide

Based on:
- Commonwealth of Virginia, Department of Medical Assistance Services (DMAS)
- EDI 834 Companion Guide Version 2.8 (September 14, 2022)
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from app.database_treo import SessionLocalTreo
from app.models.treo_models import Client, LOB


def seed_virginia_medicaid():
    """Create Virginia Medicaid client and associated LOBs."""
    db: Session = SessionLocalTreo()
    
    try:
        # Check if client already exists
        existing_client = db.query(Client).filter(Client.client_code == 'VA_MEDICAID').first()
        
        if existing_client:
            print(f"✅ Client 'VA_MEDICAID' already exists (ID: {existing_client.client_id})")
            client = existing_client
        else:
            # Create Virginia Medicaid client
            client = Client(
                client_code='VA_MEDICAID',
                client_name='Commonwealth of Virginia - Department of Medical Assistance Services (DMAS)',
                is_active=True
            )
            db.add(client)
            db.flush()  # Get client_id
            print(f"✅ Created client: {client.client_code} (ID: {client.client_id})")
        
        # Define LOBs based on EDI 834 Companion Guide
        lobs_data = [
            {
                'lob_code': 'MCO',
                'lob_name': 'Managed Care Organizations (MCOs)',
                'program_type': 'MEDICAID'
            },
            {
                'lob_code': 'MMP',
                'lob_name': 'Medicare-Medicaid Plans (MMPs)',
                'program_type': 'MEDICAID'
            },
            {
                'lob_code': 'BEHAVIORAL_HEALTH',
                'lob_name': 'Behavioral Health Service Provider',
                'program_type': 'MEDICAID'
            },
            {
                'lob_code': 'DENTAL',
                'lob_name': 'Dental Service Provider',
                'program_type': 'MEDICAID'
            },
            {
                'lob_code': 'TRANSPORTATION',
                'lob_name': 'Transportation Service Provider (NEMT Broker)',
                'program_type': 'MEDICAID'
            },
            {
                'lob_code': 'CCC_PLUS',
                'lob_name': 'CCC Plus Plans',
                'program_type': 'MEDICAID'
            },
            {
                'lob_code': 'MEDALLION_4',
                'lob_name': 'Medallion 4.0 Plans',
                'program_type': 'MEDICAID'
            }
        ]
        
        # Create or update LOBs
        created_count = 0
        updated_count = 0
        
        for lob_data in lobs_data:
            existing_lob = db.query(LOB).filter(
                LOB.client_id == client.client_id,
                LOB.lob_code == lob_data['lob_code']
            ).first()
            
            if existing_lob:
                # Update existing LOB
                existing_lob.lob_name = lob_data['lob_name']
                existing_lob.program_type = lob_data['program_type']
                existing_lob.is_active = True
                updated_count += 1
                print(f"  ✓ Updated LOB: {existing_lob.lob_code} (ID: {existing_lob.lob_id})")
            else:
                # Create new LOB
                lob = LOB(
                    client_id=client.client_id,
                    lob_code=lob_data['lob_code'],
                    lob_name=lob_data['lob_name'],
                    program_type=lob_data['program_type'],
                    is_active=True
                )
                db.add(lob)
                db.flush()  # Get lob_id
                created_count += 1
                print(f"  ✓ Created LOB: {lob.lob_code} (ID: {lob.lob_id})")
        
        # Commit all changes
        db.commit()
        
        print(f"\n✅ Seeding completed:")
        print(f"   - Client: {client.client_code}")
        print(f"   - LOBs created: {created_count}")
        print(f"   - LOBs updated: {updated_count}")
        print(f"   - Total LOBs: {created_count + updated_count}")
        
        return client
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding data: {str(e)}")
        raise
    finally:
        db.close()


if __name__ == '__main__':
    print("=" * 70)
    print("Seeding Virginia Medicaid Client and LOBs")
    print("=" * 70)
    print()
    
    seed_virginia_medicaid()
    
    print()
    print("=" * 70)
    print("Done!")
    print("=" * 70)
