import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.environ["DATABASE_DEFAULT_ENGINE"],
        'HOST': os.environ["DATABASE_DEFAULT_HOST"],
        'PORT': os.environ["DATABASE_DEFAULT_PORT"],
        'NAME': os.environ["DATABASE_DEFAULT_NAME"],
        'USER': os.environ["DATABASE_DEFAULT_USER"],
        'PASSWORD': os.environ["DATABASE_DEFAULT_PASSWORD"],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ["SECRET_KEY"] if os.environ["SECRET_KEY"] else ''

DEBUG = os.environ["DEBUG"].lower() == "true" if os.environ["DEBUG"] else False

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = [os.environ["ALLOWED_HOSTS"]] if os.environ["ALLOWED_HOSTS"] else []


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
