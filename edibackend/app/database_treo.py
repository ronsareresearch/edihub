"""
[TREO] - Treo Enrollment Database Configuration
Date: 2026-01-16
Purpose: Database configuration and session management for enroll database
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config_treo import settings_treo

# Create database engine for enroll database
# Database default timezone is set to America/New_York at database level
engine = create_engine(
    settings_treo.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=settings_treo.DEBUG,
    connect_args={
        "options": "-c search_path=public"
    }
)

# Create session factory
SessionLocalTreo = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for Treo models
BaseTreo = declarative_base()


def get_db_treo():
    """
    Dependency for getting Treo database session
    Yields a database session and closes it after use
    """
    db = SessionLocalTreo()
    try:
        yield db
    finally:
        db.close()


# Export for use in scripts
__all__ = ['BaseTreo', 'SessionLocalTreo', 'engine', 'get_db_treo']
