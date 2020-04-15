from .settings import *

ALLOWED_HOSTS = (os.environ["ALLOWED_HOST"],)

MEDIA_PATH = os.environ["MEDIA_PATH"]
MEDIA_URL = os.environ["MEDIA_URL"]

STATIC_PATH = os.environ["STATIC_PATH"]
STATIC_URL = os.environ["STATIC_URL"]

SECRET_KEY = os.environ["SECRET_KEY"]
