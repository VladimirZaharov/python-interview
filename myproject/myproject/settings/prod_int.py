from .prod import *

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'vova',
        'PASSWORD': '0',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}