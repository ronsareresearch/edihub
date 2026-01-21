#!/bin/bash

# View Docker logs

SERVICE=${1:-postgres}

echo "Viewing logs for: $SERVICE"
echo "Press Ctrl+C to exit"
echo ""

docker-compose logs -f $SERVICE

