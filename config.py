class Config(object):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'test',
        'host': 'localhost',
        'port': 27017
}

class DevConfig(Config):
    {
    }
