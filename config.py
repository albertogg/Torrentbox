class DevelopmentConfig(object):
    """docstring for config"""

    CSRF_ENABLED = True
    DEBUG = True
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskapp'


class ProductionConfig(object):
    """docstring for ClassName"""

    CSRF_ENABLED = True
    DEBUG = True
    SECRET_KEY = '({\x15w"J\xdfCl\xcdKO\xb8\x95\x1a\xec\xf7\xd0\x9d\xb9#\xd6!\x02'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskapp_pro'
