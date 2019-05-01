from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
#ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(',')
ALLOWED_HOSTS = ['*']
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')