from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: ควรย้าย SECRET_KEY ไปไว้ใน environment variable สำหรับ production
SECRET_KEY = 'django-insecure-&)@5u+$8cjx9!p+u0@jo^-#&8@*5caoje-3a9$_#^i73*@+$c*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # TODO: ตั้งเป็น False สำหรับ production

# TODO: แก้ไข ALLOWED_HOSTS สำหรับ production
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'myapp', # แอปหลักของคุณ
    'rest_framework',
    'widget_tweaks',

    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Provider ที่ต้องการ (เช่น Google)
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # Allauth middleware (ถ้ามีแนะนำในเอกสาร allauth สำหรับเวอร์ชันที่คุณใช้)
    # 'allauth.account.middleware.AccountMiddleware', # ตรวจสอบเอกสาร allauth สำหรับความจำเป็น
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), # <-- ตรวจสอบว่ามีบรรทัดนี้
            os.path.join(BASE_DIR, 'myapp/templates'), #
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', #
                'django.contrib.auth.context_processors.auth', #
                'django.contrib.messages.context_processors.messages', #
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# **สำคัญ: แก้ไขการตั้งค่า Database ให้ตรงกับ docker-compose.yml**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'django_db'),
        'USER': os.environ.get('POSTGRES_USER', 'django_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'django_pass'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'), # 'db' คือชื่อ service ใน docker-compose
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'th' # เปลี่ยนเป็น 'th' หรือ 'en-us' ตามต้องการ

TIME_ZONE = 'Asia/Bangkok' # เปลี่ยน Time Zone

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # ตรวจสอบว่าโฟลเดอร์นี้มีอยู่จริง
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_collected') # สำหรับ collectstatic ตอน deploy

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django Allauth settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Default Django auth
    'allauth.account.auth_backends.AuthenticationBackend', # Allauth specific
]

SITE_ID = 1 # จำเป็นสำหรับ allauth

# Account settings (allauth)
ACCOUNT_EMAIL_VERIFICATION = 'optional' # 'mandatory' หรือ 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False # ตั้งเป็น False ถ้าต้องการให้ email เป็น username หลัก
ACCOUNT_SIGNUP_FORM_CLASS = None # ถ้าต้องการฟอร์มสมัครสมาชิกแบบกำหนดเอง
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = False # เพื่อความปลอดภัย ควรเป็น False และใช้ POST request สำหรับ logout

# Social Account settings (allauth)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # ไม่ต้องใส่ APP ที่นี่ถ้าคุณจะตั้งค่าผ่าน Django Admin (SocialApp)
        # 'APP': {
        #     'client_id': 'YOUR_GOOGLE_CLIENT_ID',
        #     'secret': 'YOUR_GOOGLE_CLIENT_SECRET_KEY',
        #     'key': ''
        # },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# SOCIALACCOUNT_AUTO_SIGNUP = True # (Optional) ถ้าต้องการให้สมัครสมาชิกอัตโนมัติเมื่อ login ด้วย social account ครั้งแรก
# SOCIALACCOUNT_ADAPTER = 'myapp.adapter.MySocialAccountAdapter' # (Optional) ถ้าต้องการปรับแต่งพฤติกรรม social login

# Login and Logout redirect URLs
# django-allauth จะใช้ค่าเหล่านี้ แต่ก็สามารถ override ผ่าน templates ของ allauth ได้
LOGIN_REDIRECT_URL = 'home' # URL name หรือ path
LOGOUT_REDIRECT_URL = 'home' # URL name หรือ path

# Email backend (สำหรับการทดสอบ อาจใช้ console backend)
# TODO: ตั้งค่า Email Backend ที่ถูกต้องสำหรับ production (เช่น SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'