#!/bin/bash
# Deployment script for SE302 Homework 01

echo "🚀 Deploying to GitHub..."
echo ""

# Check if lock file exists and remove it
if [ -f .git/index.lock ]; then
    echo "Removing lock file..."
    rm -f .git/index.lock
fi

# Add all files
echo "Adding files to git..."
git add .

# Check status
echo ""
echo "Files to be committed:"
git status --short

# Commit
echo ""
echo "Committing changes..."
git commit -m "Initial commit: SE302 Homework 01 with unified web application

- Complete homework solution (Tasks 1, 2, 3)
- Unified web application with dark glassmorphic theme
- All test cases and bug reports included
- Deployment ready with Procfile and requirements.txt"

# Push to GitHub
echo ""
echo "Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Deployment complete!"
echo ""
echo "⚠️  Note: GitHub Pages doesn't support Flask apps."
echo "   To deploy your web app, use:"
echo "   1. Render.com (free): https://render.com"
echo "   2. Railway.app (free tier): https://railway.app"
echo ""
echo "   See DEPLOYMENT.md for detailed instructions."

