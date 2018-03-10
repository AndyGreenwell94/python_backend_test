"""This module is used to store apps separately for better readability"""

# Local apps
LOCAL_APPS = (
    'apps.series',
)

INSTALLED_APPS = (
    # Default django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'rest_framework',
) + LOCAL_APPS
