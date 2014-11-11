"""
Django settings for leavemanagement project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
def absolute_path(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'leavemanagement.settings'

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = 'AKIAIO5MLEWONX4ZNXHA'
EMAIL_HOST_PASSWORD = 'Ao7zXH53i3GJEV2zeCcoIv/5TTkd/btRKBGHJ6cKsgZI'
EMAIL_PORT = '465'
EMAIL_USE_TLS = True
ALLOWED_HOSTS = ['*']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '86li*uu#l4-$p^e5n__@8+#@!-2adu(sffmpo1!-dsvmh33vsv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
TEMPLATE_DIRS=absolute_path('../templates')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leaveform',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
)

ROOT_URLCONF = 'leavemanagement.urls'

WSGI_APPLICATION = 'leavemanagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'leavemanagement',
        'USER': '',
        'PASSWORD':'',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',)
STATICFILES_DIRS =(
     '%s'%(os.path.join(os.getcwd(),'static')),
)