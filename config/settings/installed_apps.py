"""This module is used to store apps separately for better readability"""


LOCAL_APPS = (
    'apps.series',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
) + LOCAL_APPS
