#!/bin/bash
# Script to start the EDI 834 Parser project

echo "========================================="
echo "Starting EDI 834 Parser Project"
echo "========================================="
echo ""

# Step 1: Start Docker services
echo "Step 1: Starting PostgreSQL database..."
docker-compose up -d

if [ $? -ne 0 ]; then
    echo "⚠️  Docker permission issue. Try: sudo docker-compose up -d"
    exit 1
fi

echo "✓ Waiting for database to be ready..."
sleep 5

# Step 2: Run migrations
echo ""
echo "Step 2: Running database migrations..."
cd edibackend
uv run alembic upgrade head

if [ $? -ne 0 ]; then
    echo "⚠️  Migration failed. Check database connection."
    exit 1
fi

echo "✓ Migrations completed"
cd ..

# Step 3: Start backend
echo ""
echo "Step 3: Starting backend server..."
echo "   Backend will run at: http://localhost:8000"
echo "   API docs at: http://localhost:8000/docs"
echo ""
cd edibackend
echo "   Starting uvicorn..."
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Step 4: Start frontend
echo ""
echo "Step 4: Starting frontend..."
echo "   Frontend will run at: http://localhost:3000"
echo ""
cd edifrontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "   Installing dependencies..."
    npm install
fi

echo "   Starting Vite dev server..."
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "========================================="
echo "✓ Project started successfully!"
echo "========================================="
echo ""
echo "Backend:  http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""

# Wait for user interrupt
trap "echo ''; echo 'Stopping services...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; docker-compose down; echo '✓ Services stopped'; exit" INT TERM

wait

