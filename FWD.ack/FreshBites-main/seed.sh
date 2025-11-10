#!/bin/bash

# FreshBites - Seed Database Script
# This script populates MongoDB with sample vendor and deal data

echo "🚀 Starting FreshBites Database Seeding..."
echo ""

# Check if MongoDB is running
if ! command -v mongod &> /dev/null; then
    echo "⚠️  MongoDB is not installed or not in PATH"
    echo "Please install MongoDB or ensure it's running"
    exit 1
fi

# Navigate to backend directory
cd backend || { echo "❌ Backend directory not found"; exit 1; }

# Check if seedData.js exists
if [ ! -f "seedData.js" ]; then
    echo "❌ seedData.js not found in backend directory"
    exit 1
fi

# Run the seed script
echo "📊 Populating database with sample data..."
node seedData.js

# Check if seeding was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Database seeded successfully!"
    echo ""
    echo "📝 Sample Login Credentials:"
    echo "   Email: mtr@freshbites.com"
    echo "   Password: vendor123"
    echo ""
    echo "💡 You can login with any vendor email from the following list:"
    echo "   - mtr@freshbites.com"
    echo "   - vidyarthibhavan@freshbites.com"
    echo "   - brahmins@freshbites.com"
    echo "   - maiyas@freshbites.com"
    echo "   - upahara@freshbites.com"
    echo "   - vegarama@freshbites.com"
    echo "   - nandhini@freshbites.com"
    echo "   - sagarratna@freshbites.com"
    echo "   - srisagar@freshbites.com"
    echo "   - vegpalace@freshbites.com"
    echo "   - rameshwaram@freshbites.com"
    echo "   - ctr@freshbites.com"
    echo "   - kamat@freshbites.com"
    echo "   - rasovara@freshbites.com"
    echo "   - greentheory@freshbites.com"
    echo "   - greenthaali@freshbites.com"
    echo "   - onesta@freshbites.com"
    echo "   - pureveg@freshbites.com"
    echo ""
    echo "   All passwords are: vendor123"
    echo ""
else
    echo "❌ Database seeding failed"
    exit 1
fi
