# Deployment Guide

## ⚠️ Important: GitHub Pages Limitation

**GitHub Pages only supports static HTML/CSS/JavaScript sites.** Since this is a Flask application with backend API endpoints, it **cannot run on GitHub Pages**.

## Deployment Options

### Option 1: Render.com (Recommended - Free Tier)

1. Push your code to GitHub (see commands below)
2. Go to https://render.com
3. Sign up/Login with GitHub
4. Click "New" → "Web Service"
5. Connect your GitHub repo: `kappaborg/ST`
6. Configure:
   - **Name**: `se302-homework`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn web_app.app:app`
   - **Environment**: Python 3
7. Click "Create Web Service"
8. Your app will be live at: `https://se302-homework.onrender.com`

### Option 2: Railway.app (Alternative)

1. Push code to GitHub
2. Go to https://railway.app
3. Sign up with GitHub
4. Click "New Project" → "Deploy from GitHub"
5. Select your repo
6. Railway auto-detects Flask and deploys

### Option 3: Heroku (Free tier discontinued, paid)

Similar process but requires credit card.

## Local Development

To run locally:

```bash
cd web_app
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

Then visit: http://localhost:5000

