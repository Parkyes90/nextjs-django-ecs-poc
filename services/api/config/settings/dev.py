from .base import *


ASGI_APPLICATION = "config.asgi.asgi.dev"
DEBUG = True

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

REST_FRAMEWORK = {
    # YOUR SETTINGS
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "NEXT_JS_WITH_DJANGO",
    "DESCRIPTION": "DEMO PROJECT",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    # OTHER SETTINGS
}
