import os

from environs import Env

env = Env()
env.read_env()
 
DATABASES = {
    'default': {
        'ENGINE': env.str('DEFAULT_DATABASE_ENGINE'),
        'HOST': env.str('DEFAULT_DATABASE_HOST'),
        'PORT': env.int('DEFAULT_DATABASE_PORT'),
        'NAME': env.str('DEFAULT_DATABASE_NAME'),
        'USER': env.str('DEFAULT_DATABASE_USER'),
        'PASSWORD': env.str('DEFAULT_DATABASE_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool('DEBUG')

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
