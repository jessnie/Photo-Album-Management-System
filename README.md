# 📸 Production-Ready Photo Album Management System

A modern, secure Photo Album Management application built with Django, featuring role-based access control, cloud storage integration, and production deployment.

## ✨ Features

- **Class-Based Views (CBVs)**: Clean, maintainable CRUD operations using Django's CBV architecture
- **Role-Based Access Control (RBAC)**: Secure user authentication and permission system
  - Regular users can upload, edit, and delete their own photos
  - Admin users can manage all photos
  - Public read access to gallery
- **Cloud Storage**: Cloudinary integration for reliable, scalable image management
- **Production-Ready**: Configured for deployment on Render with PostgreSQL
- **Responsive Design**: Modern, user-friendly interface with Bootstrap styling
- **Search & Pagination**: Browse and search through your photo collection
- **User Profiles**: Manage account information and view upload statistics

## 🛠️ Technology Stack

- **Backend**: Django 6.0.5
- **Database**: PostgreSQL
- **Storage**: Cloudinary (image upload & management)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render, WhiteNoise
- **Environment Management**: python-dotenv

## 📋 Requirements

- Python 3.9+
- PostgreSQL (production) or SQLite (development)
- Cloudinary account for image storage

## 🚀 Local Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/cloud-render.git
cd cloud-render
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your settings
# nano .env  # or use your favorite editor
```

**Required environment variables:**
- `SECRET_KEY`: Django secret key (generate one: https://djecrety.ir/)
- `DEBUG`: Set to `False` in production
- `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
- `CLOUDINARY_API_KEY`: Your Cloudinary API key
- `CLOUDINARY_API_SECRET`: Your Cloudinary API secret

### 5. Apply database migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` and register or log in to get started!

## 🔐 Getting Cloudinary Credentials

1. Sign up at [Cloudinary](https://cloudinary.com/) (free tier available)
2. Go to Dashboard → Settings → API Keys
3. Copy your Cloud Name, API Key, and API Secret
4. Add them to your `.env` file

## 📱 Project Structure

```
cloud-render/
├── gallery/                      # Main app
│   ├── migrations/              # Database migrations
│   ├── templates/gallery/       # HTML templates
│   │   ├── base.html           # Base template with navigation
│   │   ├── home.html           # Gallery view
│   │   ├── login.html          # User login
│   │   ├── register.html       # User registration
│   │   ├── profile.html        # User profile
│   │   ├── edit.html           # Edit photo
│   │   └── delete.html         # Delete confirmation
│   ├── views.py                # Class-based views with RBAC
│   ├── models.py               # Database models
│   ├── forms.py                # Django forms
│   ├── urls.py                 # URL routing
│   └── admin.py                # Django admin configuration
├── recipe_project/             # Project settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Root URL configuration
│   └── wsgi.py                 # WSGI application
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
├── .env.example               # Example environment variables
├── build.sh                   # Build script for Render
└── README.md                  # This file
```

## 🔐 Security Features

- **User Authentication**: Django's built-in authentication system
- **Permission System**: RBAC with owner verification
- **CSRF Protection**: Enabled by default
- **SQL Injection Prevention**: Using Django ORM
- **XSS Protection**: Template auto-escaping
- **Environment Variables**: Sensitive data not in version control
- **HTTPS Ready**: Configured for production SSL/TLS

## 📚 API Endpoints

### Authentication
- `GET /register/` - Register page
- `POST /register/` - Create new account
- `GET /login/` - Login page
- `POST /login/` - Authenticate user
- `GET /logout/` - Logout user

### Gallery (Requires Login)
- `GET /` - View all photos (with search & pagination)
- `POST /` - Upload new photo
- `GET /photo/<id>/` - View photo details
- `GET /photo/<id>/edit/` - Edit photo page
- `POST /photo/<id>/edit/` - Update photo
- `GET /photo/<id>/delete/` - Delete confirmation page
- `POST /photo/<id>/delete/` - Delete photo
- `GET /my-photos/` - View current user's photos

### User Management
- `GET /profile/` - View user profile
- `POST /profile/` - Update profile information

## 🚀 Deployment to Render

### 1. Create a Render account
Visit [render.com](https://render.com) and sign up

### 2. Create a new PostgreSQL database
- Go to Dashboard → Create New → PostgreSQL
- Choose free tier (512MB)
- Note the database URL and credentials

### 3. Create a new Web Service
- Connect your GitHub repository
- Select "Python"
- Build Command: `pip install -r requirements.txt && python manage.py migrate`
- Start Command: `gunicorn recipe_project.wsgi:application`

### 4. Add environment variables
In Render dashboard, add these variables:
```
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-render-app>.onrender.com
DATABASE_URL=<from-postgres-service>
CLOUDINARY_CLOUD_NAME=<your-value>
CLOUDINARY_API_KEY=<your-value>
CLOUDINARY_API_SECRET=<your-value>
```

### 5. Deploy
- Render will automatically deploy when you push to your repository's main branch
- Check deployment logs if issues occur

## 🧪 Testing

### Run tests
```bash
python manage.py test gallery
```

### Test locally before deployment
```bash
# Set DEBUG=True in .env for local testing
python manage.py runserver

# Test registration and login
# Test uploading photos
# Test editing/deleting your photos
# Test search functionality
```

## 📖 Usage Guide

### For Users

1. **Register**: Create a new account on the registration page
2. **Upload Photos**: 
   - Login to your account
   - Fill in title and description
   - Select an image file (JPG, PNG, WebP supported)
   - Click "Upload Photo"
3. **Edit Photos**: Click on a photo you uploaded to edit title/description
4. **Delete Photos**: Click the delete button to remove a photo
5. **Search**: Use the search bar to find photos by title or description
6. **View Profile**: Click your username in the navigation to see your stats

### For Administrators

1. Access Django admin at `/admin/` with superuser account
2. View all photos and users
3. Manage permissions and user roles
4. Edit or delete any photo

## 🐛 Troubleshooting

### "No such table: gallery_recipephoto"
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Cloudinary image upload fails
**Solution**: Check environment variables
```bash
echo $CLOUDINARY_CLOUD_NAME
echo $CLOUDINARY_API_KEY
```

### "DisallowedHost" error on Render
**Solution**: Update `ALLOWED_HOSTS` in settings.py or `.env`

### Static files not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic --noinput
```

## 📝 License

This project is open-source and available under the MIT License.

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues or questions, please open an issue on GitHub or contact the development team.

---

**Happy Photo Sharing! 📸**
