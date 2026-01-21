#!/bin/bash

# Stop Docker containers

echo "Stopping Docker containers..."
docker-compose down

echo "✅ Containers stopped"
echo ""
echo "To remove volumes (WARNING: deletes all data):"
echo "  docker-compose down -v"

