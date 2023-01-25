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

INSTALLED_APPS = [dotenv_values(".env")["INSTALLED_APPS"]]

SECRET_KEY = dotenv_values(".env")["SECRET_KEY"]

DEBUG = dotenv_values(".env")["DEBUG"]=='True'

ROOT_URLCONF = dotenv_values(".env")["ROOT_URLCONF"]

ALLOWED_HOSTS = [dotenv_values(".env")["ALLOWED_HOSTS"]]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': dotenv_values(".env")["TEMPLATES_BACKEND"],
        'DIRS': [os.path.join(BASE_DIR, dotenv_values(".env")["TEMPLATES_DIRS"])],
        'APP_DIRS': dotenv_values(".env")["TEMPLATES_APP_DIRS"]=='True',
    },
]


USE_L10N = dotenv_values(".env")["USE_L10N"]=='True'

LANGUAGE_CODE = dotenv_values(".env")["LANGUAGE_CODE"]

TIME_ZONE = dotenv_values(".env")["TIME_ZONE"]

USE_TZ = dotenv_values(".env")["USE_TZ"]=='True'

DEFAULT_AUTO_FIELD = dotenv_values(".env")["DEFAULT_AUTO_FIELD"]
