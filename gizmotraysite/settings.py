import os
from pathlib import Path

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security ---
SECRET_KEY = 'django-insecure-(+auz9*c)2)5&*#)zq817z=#8-w_&-x6(8)egi0w_wj&-*z8+o'
DEBUG = True  # ❗ Set to False in production
ALLOWED_HOSTS = ['gizmotray.onrender.com', 'localhost', '127.0.0.1']

# --- Installed Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'store',
    'tailwind',

    # Allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
]

SITE_ID = 1

# --- Authentication Backends ---
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ WhiteNoise middleware for static files on Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # ✅ Allauth middleware
    'allauth.account.middleware.AccountMiddleware',
]

# --- URL/WSGI ---
ROOT_URLCONF = 'gizmotraysite.urls'
WSGI_APPLICATION = 'gizmotraysite.wsgi.application'

# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static Files ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ WhiteNoise Static File Settings (required for Render)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Media Files ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Default Auto Field ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
