import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cd478662994f06e7cf04406ff27b8828'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nguyenjun2018@gmail.com'
    MAIL_PASSWORD = 'Huutuan2'
    ADMINS = ['noreply@gmail.com']
    LANGUAGES = ['en', 'es']
    POSTS_PER_PAGE = 3