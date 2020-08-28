# config.py
class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SECRET_KEY = 'Secret key goes here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
