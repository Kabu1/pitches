import os
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("flaskemailmoringa@gmail.com")
    MAIL_PASSWORD = os.environ.get("qazplm098")

    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/pitches'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}