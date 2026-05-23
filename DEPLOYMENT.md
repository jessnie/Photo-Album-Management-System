# 🚀 Deployment Guide - Render

## Complete Step-by-Step Deployment Instructions

### Prerequisites
- GitHub account with the repository pushed
- Cloudinary account with API credentials
- Render account (free tier available at render.com)

---

## Step 1: Prepare Your Repository

### 1.1 Make sure all code is committed
```bash
git add .
git commit -m "Production-ready Photo Album Management System"
git push origin main
```

### 1.2 Verify files are in place
Ensure these files exist in your repository root:
- ✅ `requirements.txt` - Python dependencies
- ✅ `build.sh` - Build script for Render
- ✅ `.env.example` - Environment variable template
- ✅ `README.md` - Project documentation
- ✅ `manage.py` - Django management script
- ✅ All app directories (gallery, recipe_project)

---

## Step 2: Set Up PostgreSQL Database on Render

### 2.1 Create a PostgreSQL instance
1. Go to [render.com](https://render.com)
2. Log in or create a new account
3. Click **+ New** button in top right
4. Select **PostgreSQL**
5. Configuration:
   - **Name**: `photo-album-db` (or your preferred name)
   - **Database**: `cloud_render`
   - **User**: `postgres` (or custom)
   - **Region**: Choose closest to your location
   - **PostgreSQL Version**: Latest
   - **Plan**: Free tier (512MB)

### 2.2 Copy connection details
After creating, copy these values (you'll need them soon):
- **Internal Database URL** (for services on Render)
- **Connection String** (with password)

---

## Step 3: Set Up Web Service on Render

### 3.1 Create a new Web Service
1. Click **+ New** → **Web Service**
2. Connect your GitHub repository
   - Select your photo-album repository
   - Leave branch as `main` (or your default branch)
   - Set build/start commands below

### 3.2 Configure build settings
- **Build Command**:
  ```bash
  pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput
  ```

- **Start Command**:
  ```bash
  gunicorn recipe_project.wsgi:application
  ```

### 3.3 Add environment variables
Click **Environment** and add these variables:

| Variable | Value | Source |
|----------|-------|--------|
| `SECRET_KEY` | [Generate here](https://djecrety.ir/) | Generate new |
| `DEBUG` | `False` | Fixed value |
| `ALLOWED_HOSTS` | `your-app.onrender.com` | From Render URL |
| `DATABASE_URL` | From PostgreSQL service | Render PostgreSQL |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name | Cloudinary Dashboard |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key | Cloudinary Dashboard |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret | Cloudinary Dashboard |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.onrender.com` | Your Render URL |

### 3.4 Link PostgreSQL database
1. In the Web Service settings, go to **Dependencies**
2. Link the PostgreSQL database you created earlier
3. Render will automatically set `DATABASE_URL`

### 3.5 Deploy
- Click **Create Web Service**
- Render will start building and deploying (takes 2-5 minutes)
- Check the **Logs** tab for any errors

---

## Step 4: Get Cloudinary Credentials

### 4.1 Sign up for Cloudinary (if not already done)
Visit [cloudinary.com](https://cloudinary.com/users/register/free) and sign up (free tier available)

### 4.2 Get your API credentials
1. Log in to Cloudinary Dashboard
2. Go to **Settings** → **API Keys**
3. Copy these three values:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

### 4.3 Add to Render environment variables
Add the three Cloudinary values to your Render Web Service environment variables

---

## Step 5: Create Admin Account

After first deployment, create a superuser account:

### Option A: Via Terminal (SSH)
1. In Render dashboard, go to your Web Service
2. Click **Connect** → **SSH**
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow prompts to create admin account

### Option B: Via Django Shell (SSH)
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'securepassword123')
```

### Option C: Via Render One-Off Job
In Render dashboard:
1. Go to **Dashboard** → your Web Service
2. Click **Create One-Off Job**
3. Command: `python manage.py createsuperuser`
4. Execute and follow prompts

---

## Step 6: Verify Deployment

### 6.1 Check if your site is live
Visit: `https://your-app.onrender.com`

You should see:
- ✅ Navigation bar with "Photo Album Manager"
- ✅ Register and Login links
- ✅ Clean, responsive design

### 6.2 Test functionality
1. **Register**: Create a test account
2. **Login**: Log in with test account
3. **Upload**: Upload a test photo
4. **Edit**: Edit the photo details
5. **Search**: Test the search functionality
6. **Admin**: Go to `/admin/` with superuser account

### 6.3 Check admin panel
Visit: `https://your-app.onrender.com/admin/`
- Log in with your superuser account
- Verify you can see users and photos

---

## Troubleshooting

### Issue: "DisallowedHost" Error
**Problem**: You see "Invalid HTTP_HOST header"

**Solution**: 
1. Go to Render dashboard → your Web Service
2. Copy the full app URL (e.g., `photo-album-2x4k.onrender.com`)
3. Go to **Environment**
4. Update `ALLOWED_HOSTS` to include your actual URL
5. Deploy again

### Issue: 500 Server Error
**Problem**: Something went wrong

**Solution**:
1. Check **Logs** in Render dashboard
2. Look for error messages
3. Common fixes:
   - Ensure `DATABASE_URL` is set
   - Ensure Cloudinary credentials are correct
   - Run migrations: SSH and execute `python manage.py migrate`

### Issue: Images not uploading
**Problem**: Upload button doesn't work

**Solution**:
1. Verify Cloudinary credentials in environment variables
2. Test Cloudinary API key is active in Cloudinary dashboard
3. Check browser console for JavaScript errors

### Issue: Database connection errors
**Problem**: "could not connect to server"

**Solution**:
1. Check `DATABASE_URL` in environment
2. Ensure PostgreSQL service is running in Render
3. Try redeploying web service

### Issue: Static files not loading (CSS/JS broken)
**Problem**: Page looks unstyled

**Solution**:
```bash
# Via SSH in Render
python manage.py collectstatic --noinput --clear
```

---

## Post-Deployment

### 1. Monitor your application
- Check Render dashboard regularly
- Monitor error logs
- Set up email alerts (Render Pro)

### 2. Regular maintenance
- Update dependencies monthly
- Check for Django security releases
- Test backups of database

### 3. Scale if needed
- Monitor resource usage
- Upgrade PostgreSQL plan if needed
- Upgrade web service plan if slow

### 4. Backup database
Render PostgreSQL includes automatic backups. To manually backup:
```bash
# Via Render dashboard or SSH
pg_dump -h $DATABASE_HOST -U $DATABASE_USER $DATABASE_NAME > backup.sql
```

---

## Next Steps

### Share your deployment
- Copy the live URL: `https://your-app.onrender.com`
- Share with friends/classmates
- Get feedback on features

### Further improvements
- Add email notifications
- Implement photo favorites
- Add sharing functionality
- Create API for mobile apps
- Set up continuous integration/deployment (CI/CD)

---

## Important Notes

⚠️ **Security Reminders:**
- Never commit `.env` file to GitHub
- Change `SECRET_KEY` regularly (regenerate at djecrety.ir)
- Use strong admin passwords
- Keep dependencies updated
- Monitor logs for suspicious activity
- Use HTTPS only (Render provides free SSL)

✅ **Production Checklist:**
- [ ] DEBUG set to False
- [ ] SECRET_KEY is unique and strong
- [ ] Database URL configured
- [ ] Cloudinary credentials added
- [ ] ALLOWED_HOSTS includes your domain
- [ ] Admin account created
- [ ] Test upload/edit/delete works
- [ ] Search functionality works
- [ ] Responsive design tested on mobile
- [ ] Admin panel accessible

---

## Support

If you encounter issues:
1. Check the [Render Docs](https://render.com/docs)
2. Check the [Django Docs](https://docs.djangoproject.com/)
3. Review error logs in Render dashboard
4. Check [Cloudinary Docs](https://cloudinary.com/documentation)

---

**Your Photo Album is now live! 🎉**

Visit: `https://your-app.onrender.com`
Admin Panel: `https://your-app.onrender.com/admin`
