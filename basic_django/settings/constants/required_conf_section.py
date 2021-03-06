REQUIRED_CONF_SECTIONS = {
    'django': ['SECRET_KEY'],
    'database': [
        'DATABASE_ENGINE',
        'DATABASE_NAME',
        'DATABASE_USER',
        'DATABASE_PASSWORD',
        'DATABASE_HOST',
        'DATABASE_PORT',
    ],
    'email': [
        'EMAIL_HOST',
        'EMAIL_HOST_USER',
        'EMAIL_HOST_PASSWORD',
        'EMAIL_PORT',
        'EMAIL_USE_TLS',
    ],
}
