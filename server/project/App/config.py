import os


class DevelopmentConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER', 'hoge'),
        'password': os.getenv('DB_PASSWORD', 'hoge'),
        'host': os.getenv('DB_HOST', 'db'),
        'database': os.getenv('DB_DATABASE', 'app')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
