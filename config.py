class DevelopmentConfig(object):
    """docstring for config"""

    CSRF_ENABLED = True
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskapp'


class ProductionConfig(object):
    """docstring for ClassName"""
    CSRF_ENABLED = True
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskapp_pro'
