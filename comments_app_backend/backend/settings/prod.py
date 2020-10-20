from envparse import env
from .dev import *


############
# SECURITY #
############

DEBUG = bool(env('DJANGO_DEBUG', ''))

SECRET_KEY = env('DJANGO_SECRET_KEY', SECRET_KEY)

# Set Domain here (eg. 'comments-app.ua')
CORS_ALLOWED_ORIGINS = [
    "https://c0110092568c.ngrok.io",
]

