import os
basedir = os.path.abspath(os.path.dirname(__file__))
    class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # encpription for the flask-wtf to protect all forms against cross-site request forgery (CSRF) attacks.
    
    #------- Flask-Mail conguration for Gmail-------
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
    ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'                  # Defines the prefix string for the subjecct
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>' # Defines the address that will be used as the sender
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')            # The recipient of the email is given in the FLASKY_ADMIN environment variable that’s loaded into a configuration variable of the same name during startup
    SQLALCHEMY_TRACK_MODIFICATIONS = False                   # setting key SQLALCHEMY_TRACK_MODIFICATIONS to False to use less memory unless signals for object changes are needed

    @staticmethod
    def init_app(app):
        pass
    
    class DevelopmentConfig(Config): # s. As an additional way to allow the application to customize its con‐ figuration, the Config class and its subclasses can define an init_app() class method that takes the application instance as an argument. For now the base Config class implements an empty init_app() method.

        DEBUG = True
        SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite') # Configuring URL of the application database as  the key SQLALCHEMY_DATABASE_URI in the Flask configuration object.

    class TestingConfig(Config):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or  'sqlite://'

    class ProductionConfig(Config):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    
    config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
    }


