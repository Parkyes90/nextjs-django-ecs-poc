from .base import *

INSTALLED_APPS += [
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

DEBUG = True

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'NEXT_JS_WITH_DJANGO',
    'DESCRIPTION': 'DEMO PROJECT',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}