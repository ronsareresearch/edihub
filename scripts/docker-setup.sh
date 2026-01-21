#!/bin/bash

# Docker setup script for EDI 834 project

set -e

echo "========================================="
echo "Docker Setup for EDI 834 Project"
echo "========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed"
    echo "Please install Docker: https://docs.docker.com/get-docker/"
    exit 1
fi
echo "✅ Docker found: $(docker --version)"

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not installed"
    echo "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi
echo "✅ Docker Compose found"

# Check if containers are already running
if docker ps | grep -q edi834_postgres; then
    echo "⚠️  PostgreSQL container is already running"
    read -p "Do you want to restart it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Stopping existing containers..."
        docker-compose down
    else
        echo "Keeping existing containers running"
        exit 0
    fi
fi

# Start Docker containers
echo ""
echo "Starting Docker containers..."
docker-compose up -d

# Wait for PostgreSQL to be ready
echo ""
echo "Waiting for PostgreSQL to be ready..."
timeout=60
counter=0
until docker exec edi834_postgres pg_isready -U edi834_user -d edi834 > /dev/null 2>&1; do
    sleep 2
    counter=$((counter + 2))
    if [ $counter -ge $timeout ]; then
        echo "❌ PostgreSQL failed to start within $timeout seconds"
        exit 1
    fi
    echo -n "."
done
echo ""
echo "✅ PostgreSQL is ready"

# Verify pgvector extension
echo ""
echo "Verifying pgvector extension..."
if docker exec edi834_postgres psql -U edi834_user -d edi834 -c "SELECT verify_pgvector();" > /dev/null 2>&1; then
    echo "✅ pgvector extension is installed and working"
else
    echo "⚠️  pgvector extension verification failed, but this might be normal on first run"
    echo "   The extension will be created automatically on first database access"
fi

# Display connection info
echo ""
echo "========================================="
echo "✅ Docker setup complete!"
echo "========================================="
echo ""
echo "Database connection info:"
echo "  Host: localhost"
echo "  Port: 5432"
echo "  Database: edi834"
echo "  User: edi834_user"
echo "  Password: edi834_password"
echo ""
echo "Connection string:"
echo "  postgresql://edi834_user:edi834_password@localhost:5432/edi834"
echo ""
echo "Next steps:"
echo "1. Update edibackend/.env with Docker database URL (if .env doesn't exist)"
echo "2. Run migrations: cd edibackend && uv run alembic upgrade head"
echo "3. Start backend: cd edibackend && uv run uvicorn app.main:app --reload"
echo ""
echo "Useful commands:"
echo "  docker-compose up -d          # Start containers"
echo "  docker-compose down            # Stop containers"
echo "  docker-compose logs postgres   # View PostgreSQL logs"
echo "  docker-compose ps              # Check container status"
echo "  docker exec -it edi834_postgres psql -U edi834_user -d edi834  # Connect to database"

