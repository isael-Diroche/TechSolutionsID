from .base_settings import *
from django.contrib.messages import constants as mensajes_de_error

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuraciones del Gmail

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "isaeldiroche00@gmail.com"
EMAIL_HOST_PASSWORD = "mmhxgqexbxslhnuf"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}



# Otras configuraciones específicas del entorno de desarrollo...
