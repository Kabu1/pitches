#import os
#import app
class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/watchlist'
    SECRET_KEY ='qwerty1234'
#  email configurations
    #app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   # app.config['MAIL_PORT'] = 587
   # app.config['MAIL_USE_TLS'] = True
   # app.config['MAIL_USERNAME'] = "flaskemailmoringa@gmail.com"
   # app.config['MAIL_PASSWORD'] = "qazplm098"

    

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

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}