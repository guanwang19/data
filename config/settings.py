import os
from dotenv import load_dotenv
from pathlib import Path

def global_context(request):
    return {"courses": Course.objects.all()}
# Load environment variables
load_dotenv()

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Get SECRET_KEY from .env
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")

AUTH_USER_MODEL = "users.User"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'course_db',
        'USER': 'django_user',
        'PASSWORD': 'post2025',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True  # If this is False, you must set ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Add your domain/IP if needed

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # ✅ Custom apps
    'users',
    'courses',
    'cart',
    'payments',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# config/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ Ensure this exists
        'APP_DIRS': True,  # ✅ Django should look inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Define the root URL configuration
ROOT_URLCONF = "config.urls"

# Static files settings
STATIC_URL = "/static/"  # Required for serving static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "config/static",  # Add this line if config/static exists
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ Corrected Video URL and Root Directory
VIDEO_URL = "/videos/"
VIDEO_ROOT = os.path.join(BASE_DIR, "videos")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "gaunwang19@gmail.com"  # ✅ Admin email (host)
EMAIL_HOST_PASSWORD = "edkadtucpqzqwkyw"  # ✅ App password (DO NOT store directly in settings; use env variables)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # ✅ This ensures the admin gets the reset email

