from .development import *

SECRET_KEY = '+bf56&8+okokr9u!i=%b0mt7oad2^e(a-m-%#a(6rkbkz84rnc'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
