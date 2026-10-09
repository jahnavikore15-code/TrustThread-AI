@echo off
cd /d "%~dp0"
echo Starting TrustThread AI...
echo.
echo If Docker Desktop is installed, this starts PostgreSQL + FastAPI + React.
docker compose up --build
pause
