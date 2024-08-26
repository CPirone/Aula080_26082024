import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

# Carregar .env com caminho absoluto
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'hard_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'data.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    FIXED_RECIPIENTS = os.getenv('FIXED_RECIPIENTS', '').split(',')
    FIXED_FROM = os.getenv('FIXED_FROM')

    @staticmethod
    def init_app(app):
        pass

config = {
    'default': Config
}
