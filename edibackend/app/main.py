"""
[TREO] - FastAPI Application Entry Point
[UPDATED] - 2026-01-16: YAML/JSON-only architecture - Treo API only
Date: 2026-01-16
Purpose: FastAPI application entry point - Treo enrollment API (YAML/JSON architecture)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api_treo import router as treo_router

# Create FastAPI app
app = FastAPI(
    title="Treo Enrollment - EDI 834 Parser",
    description="YAML/JSON-based EDI 834 parsing and validation",
    version="2.0.0"
)

# Add CORS middleware for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Treo API routes (YAML/JSON architecture)
app.include_router(treo_router, prefix="/api/v1/treo", tags=["Treo Enrollments"])

__all__ = ['app']
