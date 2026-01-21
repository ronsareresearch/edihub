"""
[TREO] - Treo Enrollment Configuration
Date: 2026-01-16
Purpose: Application configuration for enroll database
"""
from pydantic_settings import BaseSettings
from pathlib import Path


class SettingsTreo(BaseSettings):
    """Application settings for Treo enrollment architecture"""
    
    # Application
    APP_NAME: str = "Treo Digital Health Syatem"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database - enroll database
    # Use TREO_DATABASE_URL from env, fallback to default
    TREO_DATABASE_URL: str = "postgresql://edi834_user:edi834_password@localhost:5432/enroll"
    
    @property
    def DATABASE_URL(self) -> str:
        """Get Treo database URL"""
        return self.TREO_DATABASE_URL
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"  # Ignore extra fields from .env file


# Initialize Treo settings
settings_treo = SettingsTreo()
