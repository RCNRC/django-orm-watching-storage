import os
from dotenv import dotenv_values

DATABASES = {
    'default': {
        'ENGINE': dotenv_values(".env")["DATABASES_DEFAULT_ENGINE"],
        'HOST': dotenv_values(".env")["DATABASES_DEFAULT_HOST"],
        'PORT': dotenv_values(".env")["DATABASES_DEFAULT_PORT"],
        'NAME': dotenv_values(".env")["DATABASES_DEFAULT_NAME"],
        'USER': dotenv_values(".env")["DATABASES_DEFAULT_USER"],
        'PASSWORD': dotenv_values(".env")["DATABASES_DEFAULT_PASSWORD"],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = dotenv_values(".env")["SECRET_KEY"]

DEBUG = True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
