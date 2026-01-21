"""
[ENROLL] - Alembic Environment Configuration
Date: 2026-01-20
Purpose: Alembic environment for enroll database migrations
"""
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Import Treo models and metadata models
from app.database_treo import BaseTreo as Base
from app.models.treo_models import (
    Client, LOB, EnrollmentFile, ProcessLog
)
from app.models.treo_metadata import (
    Loop, Segment, Element, ElementDataType, IndustryUsage,
    SyntaxRule, Syntax, LoopSegment, LoopElement, CodeValue,
    LoopElementAdditionalSyntax, ControlSegment, ControlSegmentElement,
    ControlSegmentCodeValue, ControlSegmentElementData,
    ElementDataTypeExpression, ElementComment
)

# This is the Alembic Config object
config = context.config

# Set database URL from Treo settings if not already set
if not config.get_main_option("sqlalchemy.url"):
    from app.config_treo import settings_treo
    config.set_main_option("sqlalchemy.url", settings_treo.DATABASE_URL)

# Note: Migrations are stored directly in the migrations directory (not in a versions subdirectory)
# This is configured via version_path in context.configure() calls below

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    migrations_dir = Path(__file__).parent
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_path=str(migrations_dir),  # Use migrations directory directly (not versions subdirectory)
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        migrations_dir = Path(__file__).parent
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            version_path=str(migrations_dir),  # Use migrations directory directly (not versions subdirectory)
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
