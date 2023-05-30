import os
from environs import Env

env = Env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('SRV_HOST'),
        'PORT': env.int('SRV_PORT'),
        'NAME': env.str('SRV_NAME'),
        'USER': env.str('SRV_USER'),
        'PASSWORD': env.str('SRV_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']
ROOT_URLCONF = 'project.urls'
ALLOWED_HOSTS = [env.str('SRV_ALLOWED_HOSTS')]


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