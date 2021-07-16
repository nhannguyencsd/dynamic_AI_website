import json

with open('/etc/config.json') as config_file:
        config = json.load(config_file)

class Configuration():
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    REDIS_URI = config.get('REDIS_URI') # use redis backend storage for flask-limiter
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL_ADDRESS')
    MAIL_PASSWORD = config.get('EMAIL_PASSWORD')

class DevelopmentConfiguration(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config.get('DEVELOPMENT_DATABASE_URL') # postgresql development database

class ProductionConfiguration(Configuration):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config.get('PRODUCTION_DATABASE_URL') # postgresql production database

configuration = {
    'development': DevelopmentConfiguration,
    'production': ProductionConfiguration
}