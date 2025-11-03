@echo off
REM FreshBites - Seed Database Script for Windows
REM This script populates MongoDB with sample vendor and deal data

echo.
echo ========================================
echo  FreshBites Database Seeding
echo ========================================
echo.

REM Navigate to backend directory
cd backend
if errorlevel 1 (
    echo ERROR: Backend directory not found
    exit /b 1
)

REM Check if seedData.js exists
if not exist "seedData.js" (
    echo ERROR: seedData.js not found in backend directory
    cd ..
    exit /b 1
)

REM Run the seed script
echo Populating database with sample data...
echo.
node seedData.js

if errorlevel 1 (
    echo.
    echo ERROR: Database seeding failed
    cd ..
    exit /b 1
)

cd ..

echo.
echo ========================================
echo  Database Seeded Successfully!
echo ========================================
echo.
echo Sample Login Credentials:
echo    Email: mtr@freshbites.com
echo    Password: vendor123
echo.
echo You can login with any vendor email:
echo    - mtr@freshbites.com
echo    - vidyarthibhavan@freshbites.com
echo    - brahmins@freshbites.com
echo    - maiyas@freshbites.com
echo    - upahara@freshbites.com
echo    - vegarama@freshbites.com
echo    - nandhini@freshbites.com
echo    - sagarratna@freshbites.com
echo    - srisagar@freshbites.com
echo    - vegpalace@freshbites.com
echo    - rameshwaram@freshbites.com
echo    - ctr@freshbites.com
echo    - kamat@freshbites.com
echo    - rasovara@freshbites.com
echo    - greentheory@freshbites.com
echo    - greenthaali@freshbites.com
echo    - onesta@freshbites.com
echo    - pureveg@freshbites.com
echo.
echo All passwords are: vendor123
echo.
pause
