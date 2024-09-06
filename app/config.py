import os

class Config: 
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/vision_master'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_TIMEOUT = 300
    WTF_CSRF_CHECK_DEFAULT = False
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_SECRET_KEY = 'super-secret'
    CORS_HEADERS = 'Content-Type'
    CORS_HEADERS = 'Authorization'