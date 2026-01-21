"""
Reset Enrollment Files Table
Date: 2026-01-20
Purpose: Truncate enrollment_files table and reset sequence to 1
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database_treo import SessionLocalTreo
from sqlalchemy import text


def reset_enrollment_files(reset_sequence: bool = True):
    """
    Truncate enrollment_files table and optionally reset sequence.
    
    Args:
        reset_sequence: If True, reset sequence to 1 (default: True)
    """
    db = SessionLocalTreo()
    try:
        print("=" * 80)
        print("Resetting Enrollment Files Table")
        print("=" * 80)
        
        # Get count before
        count_before = db.execute(text("SELECT COUNT(*) FROM public.enrollment_files")).scalar()
        print(f"Records before: {count_before}")
        
        # Get sequence value before
        seq_value_before = db.execute(
            text("SELECT last_value FROM public.enrollment_files_enrollment_file_id_seq")
        ).scalar()
        print(f"Sequence value before: {seq_value_before}")
        
        # Truncate table with RESTART IDENTITY to reset sequence
        # Note: RESTART IDENTITY must come before CASCADE in PostgreSQL syntax
        if reset_sequence:
            db.execute(text("TRUNCATE TABLE public.enrollment_files RESTART IDENTITY CASCADE"))
            print("\n✅ Truncated table with RESTART IDENTITY (sequence reset to 1)")
        else:
            db.execute(text("TRUNCATE TABLE public.enrollment_files CASCADE"))
            print("\n✅ Truncated table (sequence NOT reset - will continue from previous value)")
        
        db.commit()
        
        # Get sequence value after
        seq_value_after = db.execute(
            text("SELECT last_value FROM public.enrollment_files_enrollment_file_id_seq")
        ).scalar()
        print(f"Sequence value after: {seq_value_after}")
        
        # Verify
        count_after = db.execute(text("SELECT COUNT(*) FROM public.enrollment_files")).scalar()
        print(f"Records after: {count_after}")
        
        print("\n✅ Reset complete!")
        print("=" * 80)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        db.rollback()
        return False
    finally:
        db.close()


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Reset enrollment_files table')
    parser.add_argument(
        '--no-reset-sequence',
        action='store_true',
        help='Truncate table but do NOT reset sequence'
    )
    
    args = parser.parse_args()
    
    success = reset_enrollment_files(reset_sequence=not args.no_reset_sequence)
    sys.exit(0 if success else 1)
