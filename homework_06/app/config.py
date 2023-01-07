from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql://username:userpass@localhost:5432/blog",
)

SECRET_KEY = getenv(
    "SECRET_KEY",
    "sdfsdfsdfsdgwrtwegsdgsg",
)


class Config:
    ENV = ""
    DEBUG = False
    Testing = False
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    Testing = True
