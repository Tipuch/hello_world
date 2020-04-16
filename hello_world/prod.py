from .settings import *

ALLOWED_HOSTS = (os.environ["ALLOWED_HOST"],)

MEDIA_ROOT = os.environ["MEDIA_ROOT"]
MEDIA_URL = os.environ["MEDIA_URL"]

STATIC_ROOT = os.environ["STATIC_ROOT"]
STATIC_URL = os.environ["STATIC_URL"]

SECRET_KEY = os.environ["SECRET_KEY"]
