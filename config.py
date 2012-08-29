class DevelopmentConfig(object):
    """docstring for config"""

    CSRF_ENABLED = True
    DEBUG = True
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskapp'


class ProductionConfig(object):
    """docstring for ClassName"""

    CSRF_ENABLED = True
    DEBUG = False
    # Change the secret key for security.
    SECRET_KEY = 'my_secret_production_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskapp_production'
