# TREO Digital Health System - EDI 834 Enrollment Parser

A comprehensive system for parsing, validating, and managing EDI 834 (Benefit Enrollment and Maintenance) files for healthcare enrollment management.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Frontend Features](#frontend-features)
- [Database Schema](#database-schema)
- [Development](#development)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

## Overview

The TREO Digital Health System is designed to process EDI 834 files, which are the standard format for electronic enrollment and maintenance of health insurance benefits. The system provides:

- **EDI 834 File Parsing**: Converts EDI files to structured JSON format
- **Data Validation**: Validates EDI structure and business rules
- **Database Storage**: Stores parsed data in normalized PostgreSQL tables
- **Analytics**: Provides comprehensive analytics on processed files
- **Web Interface**: User-friendly React frontend for file upload and data visualization
- **RESTful API**: Complete API for programmatic access

### Key Features

- ✅ Streaming parser for large files (1M+ members)
- ✅ Duplicate file detection
- ✅ Comprehensive error and warning logging
- ✅ Multiple transaction set support
- ✅ LS/LE loop handling (Additional Reporting Categories)
- ✅ Real-time processing status updates
- ✅ Analytics dashboard with member statistics
- ✅ File-based JSON storage for full data access

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (React)                        │
│  - File Upload UI                                           │
│  - Processing Stepper                                       │
│  - Analytics Dashboard                                       │
│  - Data Visualization                                       │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/REST
┌──────────────────────▼──────────────────────────────────────┐
│                  Backend (FastAPI)                          │
│  - API Endpoints                                            │
│  - Request Validation                                       │
│  - Business Logic                                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌────▼──────┐ ┌────▼──────┐
│   Parser     │ │  Services  │ │  Models   │
│  (Streaming) │ │ (Business) │ │ (SQLAlch) │
└───────┬──────┘ └────┬──────┘ └────┬──────┘
        │              │              │
        └──────────────┼──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │   PostgreSQL Database       │
        │  - Metadata Schema           │
        │  - Public Schema             │
        │  - EDI Data Tables           │
        └─────────────────────────────┘
```

### Data Flow

1. **Upload**: User uploads EDI 834 file via frontend
2. **Parse**: Streaming parser processes file segment by segment
3. **Validate**: Business rules and structure validation
4. **Store**: Data stored in normalized database tables
5. **JSON**: Full JSON structure saved to file system
6. **Analytics**: Statistics generated and displayed

## Technology Stack

### Backend
- **Python 3.8+**
- **FastAPI** - Modern, fast web framework
- **SQLAlchemy 2.0** - ORM for database operations
- **Alembic** - Database migration tool
- **PostgreSQL 16** - Relational database
- **Pydantic** - Data validation
- **uv** - Fast Python package manager

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Material-UI (MUI)** - Component library
- **Vite** - Build tool and dev server
- **Axios** - HTTP client
- **React Router** - Client-side routing

### Infrastructure
- **Docker** - Containerization (PostgreSQL)
- **Docker Compose** - Multi-container orchestration

## Project Structure

```
DigitialHealthSystem/
├── edibackend/                 # Backend application
│   ├── app/
│   │   ├── api_treo.py        # API endpoints
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── config_treo.py     # Configuration
│   │   ├── database_treo.py   # Database connection
│   │   ├── models/            # SQLAlchemy models
│   │   │   ├── treo_models.py      # Main models
│   │   │   ├── treo_metadata.py    # Metadata models
│   │   │   └── treo_member_models.py
│   │   └── services/          # Business logic
│   │       ├── treo_parser_834.py          # Main parser
│   │       ├── treo_streaming_parser_834.py # Streaming parser
│   │       ├── edi_data_service.py         # Data services
│   │       ├── analytics/                  # Analytics service
│   │       └── ...
│   ├── migrations/            # Database migrations
│   │   ├── env.py             # Alembic environment
│   │   └── *.py               # Migration files
│   ├── scripts/               # Utility scripts
│   │   ├── master_migration.py    # Master migration script
│   │   └── seed_virginia_medicaid.py
│   ├── data/                  # Data storage
│   │   └── json_files/        # Parsed JSON files
│   ├── requirements.txt       # Python dependencies
│   └── pyproject.toml        # Project configuration
│
├── edifrontend/               # Frontend application
│   ├── src/
│   │   ├── pages/            # React pages
│   │   │   ├── TreoUpload.tsx    # Upload page
│   │   │   ├── TreoView.tsx      # Data view page
│   │   │   └── TreoAnalytics.tsx # Analytics page
│   │   ├── services/         # API services
│   │   │   └── treoService.ts
│   │   ├── App.tsx           # Main app component
│   │   └── main.tsx          # Entry point
│   ├── package.json          # Node dependencies
│   └── vite.config.ts        # Vite configuration
│
├── docker-compose.yml        # Docker services
├── START_PROJECT.sh          # Quick start script
├── .gitignore                # Git ignore rules
├── .dockerignore             # Docker ignore rules
└── README.md                 # This file
```

## Prerequisites

- **Python 3.8+** with `uv` package manager
- **Node.js 18+** and npm
- **PostgreSQL 16+** (or Docker)
- **Docker** and Docker Compose (for database)
- **Git**

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd DigitialHealthSystem
```

### 2. Install Backend Dependencies

```bash
cd edibackend
uv sync
```

### 3. Install Frontend Dependencies

```bash
cd ../edifrontend
npm install
```

### 4. Set Up Environment Variables

Create `edibackend/.env` (optional - defaults are provided):

```env
TREO_DATABASE_URL=postgresql://edi834_user:edi834_password@localhost:5432/enroll
```

## Configuration

### Database Configuration

The default database configuration is in `edibackend/app/config_treo.py`:

- **Database**: `enroll`
- **User**: `edi834_user`
- **Password**: `edi834_password`
- **Host**: `localhost`
- **Port**: `5432`

Override via environment variable:
```bash
export TREO_DATABASE_URL="postgresql://user:pass@host:5432/dbname"
```

### Frontend Configuration

Frontend API URL is configured in `edifrontend/src/api/client.ts`:

```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
```

Set `VITE_API_URL` in `.env` for production.

## Database Setup

### Option 1: Using Docker (Recommended)

```bash
# Start PostgreSQL container
docker-compose up -d

# Run migrations
cd edibackend
uv run alembic upgrade head

# Seed base data (optional)
uv run python scripts/master_migration.py
```

### Option 2: Using Master Migration Script

For a fresh database instance:

```bash
cd edibackend
uv run python scripts/master_migration.py
```

Options:
- `--db-url <url>` - Override database URL
- `--skip-seed` - Skip seeding base data
- `--verify-only` - Only verify setup

### Option 3: Manual Setup

1. Create PostgreSQL database:
```sql
CREATE DATABASE enroll;
CREATE USER edi834_user WITH PASSWORD 'edi834_password';
GRANT ALL PRIVILEGES ON DATABASE enroll TO edi834_user;
```

2. Run migrations:
```bash
cd edibackend
uv run alembic upgrade head
```

3. Seed base data:
```bash
uv run python scripts/seed_virginia_medicaid.py
```

## Running the Application

### Quick Start (All Services)

```bash
./START_PROJECT.sh
```

This script:
1. Starts PostgreSQL (Docker)
2. Runs database migrations
3. Starts backend server (port 8000)
4. Starts frontend dev server (port 3000)

### Manual Start

#### 1. Start Database

```bash
docker-compose up -d
```

#### 2. Start Backend

```bash
cd edibackend
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

#### 3. Start Frontend

```bash
cd edifrontend
npm run dev
```

Frontend will be available at:
- http://localhost:3000

## API Documentation

### Base URL
```
http://localhost:8000/api/v1/treo
```

### Endpoints

#### Upload EDI File
```http
POST /enrollments/upload
Content-Type: multipart/form-data

Parameters:
- file: EDI 834 file
- client_id: int (required)
- lob_id: int (required)
- duplicate_mode: str (optional, default: "warn")
- created_by: str (optional)
```

#### Get Enrollment File
```http
GET /enrollments/{enrollment_file_id}
```

#### Get Enrollment JSON
```http
GET /enrollments/{enrollment_file_id}/json
```

#### Get Processing Logs
```http
GET /enrollments/{enrollment_file_id}/logs?log_type=error
```

#### List Enrollments
```http
GET /enrollments?client_id=1&lob_id=1&processing_status=completed&limit=100&offset=0
```

#### Query Enrollment Data
```http
POST /enrollments/{enrollment_file_id}/query
Content-Type: application/json

{
  "query": "SELECT * FROM edi_data WHERE ref02_1 = '123456789'"
}
```

#### Get Analytics
```http
GET /enrollments/{enrollment_file_id}/analytics
```

#### Get Summary Analytics
```http
GET /analytics/summary?client_id=1&lob_id=1
```

### Interactive API Documentation

Visit http://localhost:8000/docs for Swagger UI with interactive API testing.

## Frontend Features

### Upload Page (`/`)
- File upload with drag-and-drop
- Client and LOB selection
- Duplicate detection mode selection
- Real-time processing stepper:
  - Upload File
  - Parse EDI
  - Validate Data
  - Store Results
  - Complete
- Error and warning display
- Success redirect to analytics

### Analytics Page (`/treo/analytics/:id`)
- File information
- Member statistics (total, unique, duplicates)
- Duplicate analysis table
- Segment statistics
- Transaction statistics
- LS/LE loop statistics
- Processing summary

### View Page (`/treo/view/:id`)
- Full JSON data viewer
- Expandable sections
- Download JSON file
- Processing status

## Database Schema

### Public Schema Tables

#### Core Tables
- **`clients`** - Client/tenant information
- **`lobs`** - Line of Business definitions
- **`enrollment_files`** - File metadata and status
- **`process_log`** - Processing logs, errors, warnings

#### EDI Data Tables
- **`edi_control_seg`** - ISA, GS, GE, IEA segments (one per file)
- **`edi_trans_seg`** - ST, BGN, REF, DTP, N1, SE segments (one per transaction set)
- **`edi_data`** - Member-level data (INS, REF, DTP, NM1, N3, N4, DMG, LUI, HD, AMT, LS, LE)
- **`edi_addt_data`** - Additional reporting data (LS/LE loops)

### Metadata Schema Tables

Stores EDI 834 standard metadata:
- **`loops`** - Loop definitions
- **`segments`** - Segment definitions
- **`elements`** - Element definitions
- **`code_values`** - Valid code values
- And more...

### Relationships

```
enrollment_files (1) ──< (N) edi_control_seg
enrollment_files (1) ──< (N) edi_trans_seg
enrollment_files (1) ──< (N) edi_data
enrollment_files (1) ──< (N) edi_addt_data
enrollment_files (1) ──< (N) process_log
clients (1) ──< (N) enrollment_files
lobs (1) ──< (N) enrollment_files
edi_data (1) ──< (N) edi_addt_data (via ref02_1)
```

## Development

### Backend Development

```bash
cd edibackend

# Run with auto-reload
uv run uvicorn app.main:app --reload

# Run tests (if available)
uv run pytest

# Create new migration
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Rollback migration
uv run alembic downgrade -1
```

### Frontend Development

```bash
cd edifrontend

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

### Code Style

- **Python**: Follow PEP 8, use type hints
- **TypeScript**: Use strict mode, follow ESLint rules
- **SQL**: Use Alembic migrations, no raw SQL in code

## Deployment

### Production Considerations

1. **Environment Variables**: Set all sensitive values via environment variables
2. **Database**: Use production PostgreSQL instance
3. **File Storage**: Configure proper storage for JSON files
4. **CORS**: Update CORS settings in `app/main.py`
5. **Security**: Enable HTTPS, use proper authentication
6. **Monitoring**: Set up logging and monitoring
7. **Backup**: Regular database backups

### Docker Deployment (Future)

The project structure supports containerization. To add:
1. Create `Dockerfile` for backend
2. Create `Dockerfile` for frontend
3. Update `docker-compose.yml` with app services
4. Configure production settings

## Troubleshooting

### Database Connection Issues

```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Check database connection
docker exec -it treo_postgres psql -U edi834_user -d enroll

# View database logs
docker-compose logs postgres
```

### Migration Issues

```bash
# Check current migration version
cd edibackend
uv run alembic current

# View migration history
uv run alembic history

# Reset database (WARNING: deletes all data)
uv run alembic downgrade base
uv run alembic upgrade head
```

### Port Conflicts

If ports 3000 or 8000 are in use:

**Backend:**
```bash
uv run uvicorn app.main:app --reload --port 8001
```

**Frontend:**
Update `vite.config.ts` or use:
```bash
npm run dev -- --port 3001
```

### File Processing Errors

1. Check `process_log` table for detailed errors
2. Verify EDI file format (should be valid 834)
3. Check file size (very large files may need more memory)
4. Review backend logs for exceptions

### Frontend Not Connecting to Backend

1. Verify backend is running on port 8000
2. Check CORS settings in `app/main.py`
3. Verify `VITE_API_URL` in frontend `.env`
4. Check browser console for errors

## License


## Support

For issues and questions:
- Create an issue in the repository
- Contact the development team
- Review documentation in `/docs` directory

## Contributing

---

**Version**: 2.0.0  
**Last Updated**: January 2026
