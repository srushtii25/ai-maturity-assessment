# AI Maturity Assessment - Deployment Guide

## Quick Deploy to Heroku (Recommended)

### Prerequisites
1. Install [Git](https://git-scm.com/)
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Create a [Heroku account](https://signup.heroku.com/)

### Step 1: Initialize Git Repository
```bash
cd ai_maturity_app
git init
git add .
git commit -m "Initial commit"
```

### Step 2: Create Heroku App
```bash
heroku create your-app-name-here
# Example: heroku create ai-maturity-assessment-demo
```

### Step 3: Set Environment Variables
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set MONGODB_URI="mongodb+srv://srushtinaik02:7O1uYoahid5JPyxU@aimaturitydb.ydjlbe8.mongodb.net/"
heroku config:set MONGODB_NAME="aimaturitydb"
```

### Step 4: Deploy
```bash
git push heroku main
```

### Step 5: Open Your App
```bash
heroku open
```

## Alternative: Railway Deployment

### Step 1: Install Railway CLI
```bash
npm install -g @railway/cli
```

### Step 2: Login and Deploy
```bash
railway login
railway init
railway up
```

## Alternative: Render Deployment

1. Connect your GitHub repository to [Render](https://render.com)
2. Create a new Web Service
3. Set environment variables in Render dashboard
4. Deploy automatically from GitHub

## Environment Variables Required

- `SECRET_KEY`: Django secret key (generate a new one for production)
- `DEBUG`: Set to `False` for production
- `MONGODB_URI`: Your MongoDB connection string
- `MONGODB_NAME`: Your MongoDB database name

## Important Files for Deployment

- `Procfile`: Tells Heroku how to run your app
- `requirements.txt`: Python dependencies
- `runtime.txt`: Python version specification
- `settings.py`: Updated for production
- `.env.example`: Template for environment variables

## Post-Deployment Checklist

1. ✅ App loads without errors
2. ✅ User registration works
3. ✅ Assessment flow works
4. ✅ PDF generation works
5. ✅ MongoDB connection is stable
6. ✅ Static files load correctly

## Troubleshooting

### Common Issues:
1. **Static files not loading**: Check WhiteNoise configuration
2. **MongoDB connection errors**: Verify connection string and network access
3. **PDF generation fails**: Ensure WeasyPrint dependencies are installed
4. **App crashes**: Check Heroku logs with `heroku logs --tail`

### Useful Commands:
```bash
# View logs
heroku logs --tail

# Run Django commands
heroku run python manage.py migrate

# Access Django shell
heroku run python manage.py shell

# Restart app
heroku restart
```

## Security Notes

- Never commit `.env` file to version control
- Use strong SECRET_KEY in production
- Set DEBUG=False in production
- Consider adding HTTPS redirect middleware
- Review MongoDB security settings