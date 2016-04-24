"""
Django settings for ecommerce project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '99l%rq+pa0nwgdu-szr!wfqkaz7)oj*3^@l-ado@6cccqz%ti1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_FROM_EMAIL = "Mohit for Makhija <makhija.mohit77@gmail.com>"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mohit.makhija77@gmail.com'
EMAIL_HOST_PASSWORD = 'n0vember1992'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SITE_URL = "http://omkarts.com"
if DEBUG:
    SITE_URL = "http://localhost:8000"

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    # 'south', # no longer needed
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'smart_selects',
    'import_export',
    'accounts',
    'carts',
    'marketing',
    'orders',
    'products',
    'product_description',
    'product_filters',
    'localflavor',
)

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'marketing.middleware.DisplayMarketing',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Django suit values ..
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',

            ],
        },
    },
]


WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.request",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     'django.core.context_processors.request',
#     "django.contrib.messages.context_processors.messages",
#     # 'django.core.context_processors.request',
# )

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
# MEDIA_ROOT = '/Users/Mohit/Desktop/Projects/django-projects/django-projects-learning/ecommerce/static/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
)

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates'),
# )

MARKETING_HOURS_OFFSET = 3
MARKETING_SECONDS_OFFSET = 8
DEFAULT_TAX_RATE = 0.08 # 8%

STRIPE_SECRET_KEY = "sk_test_QodCjTce39UlPRCBjvc9aqQB"
STRIPE_PUBLISHABLE_KEY = "pk_test_eoERCo5opxxiZeGP24wi7M1L"

# FACEBOOK_APP_ID='1083643738324083'
# FACEBOOK_API_SECRET='7c58021fba32e7c806e7d9d051079144'

# SITE_ID = 1

# LOGIN_REDIRECT_URL = '/'

CKEDITOR_UPLOAD_PATH = "{{media}}uploads/"

CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ["Format", "Styles", ],
            ["Bold", "Italic", "Underline", "Strikethrough", "Undo", "Redo", ],
            ["JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock", ],
            ["Link", "Unlink", ],
            ["Smiley", "SpecialChar", ],
            ["Image", "Flash", "Table", ],
            ["NumberedList", "BulletedList", ],
            ["Subscript", "Superscript", ],
            ["TextColor", ],
            ["Source", ],
        ],
        'autoParagraph': False,
    },
}

CKEDITOR_SETTINGS = {
    'default': {
        'toolbar': [
            ["Format", "Styles", ],
            ["Bold", "Italic", "Underline", "Strikethrough", "Undo", "Redo", ],
            ["JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock", ],
            ["Link", "Unlink", ],
            ["Smiley", "SpecialChar", ],
            ["Image", "Flash", "Table", ],
            ["NumberedList", "BulletedList", ],
            ["Subscript", "Superscript", ],
            ["TextColor", ],
            ["Source", ],
        ],
        'skin': 'moono',
        'autoParagraph': False,
    },
}
