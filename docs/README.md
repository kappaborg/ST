# SE302 Homework 01 - Static Web Application

This is the static version of the web application, ready for GitHub Pages deployment.

## 🚀 Deploy to GitHub Pages

1. **Push the `docs` folder to your GitHub repo**
2. **Go to your repository settings**: https://github.com/kappaborg/ST/settings/pages
3. **Under "Source"**, select **"Deploy from a branch"**
4. **Select branch**: `main`
5. **Select folder**: `/docs`
6. **Click "Save"**
7. **Your site will be live at**: `https://kappaborg.github.io/ST/`

## 📝 Note

All backend logic has been converted to JavaScript:
- Task 1: Shoe validation (client-side)
- Task 2: Library system (using localStorage)
- Task 3: Statistics functions (pure JavaScript)

## 🔧 Local Testing

To test locally before deploying:

```bash
cd docs
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

Or use any static file server.

