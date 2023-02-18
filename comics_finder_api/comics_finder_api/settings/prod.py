import environ
import os
import logging.config


from .dev import *

env = environ.Env()

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env.bool('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    'default': env.db(),
}

ALLOWED_HOSTS=env.list('ALLOWED_HOSTS')

# HTTPS !
CSRF_COOKIE_SECURE=env.bool('CSRF_COOKIE_SECURE', False)
SESSION_COOKIE_SECURE=env.bool('SESSION_COOKIE_SECURE', False)
SECURE_SSL_REDIRECT=env.bool('SECURE_SSL_REDIRECT', False)
SECURE_HSTS_SECONDS=env.bool('SECURE_HSTS_SECONDS', False)
SECURE_HSTS_INCLUDE_SUBDOMAINS=env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', False)
SECURE_HSTS_PRELOAD=env.bool('SECURE_HSTS_PRELOAD', False)


# Logging Configuration

# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console',],
        },
    },
})