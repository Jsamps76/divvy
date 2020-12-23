class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never know'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/divvy_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
