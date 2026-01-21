#!/bin/bash

# Connect to PostgreSQL database shell

echo "Connecting to PostgreSQL database..."
echo "Type '\\q' to exit"
echo ""

docker exec -it edi834_postgres psql -U edi834_user -d edi834

