import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you can not guess the key')
    CATCHAT_MESSAGE_PER_PAGE = 30
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@quickchat.com')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/quickchat'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/quickchat'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
