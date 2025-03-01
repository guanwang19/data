import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Get SECRET_KEY from .env
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")

AUTH_USER_MODEL = "users.User"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL
        'NAME': 'course_db',  # Change to your actual database name
        'USER': 'postgres',  # Change to your PostgreSQL username
        'PASSWORD': 'Ilv$post1',  # Change to your PostgreSQL password
        'HOST': 'localhost',  # Use localhost if running PostgreSQL locally
        'PORT': '5432',  # Default PostgreSQL port
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
    
    # Custom apps
    'courses',
    'users',
    'payments',
    'chatbot',
    'support',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # This now works correctly
        'APP_DIRS': True,
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
]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
