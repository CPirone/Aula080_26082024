from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')

    # Importa e registra as rotas
    from app.main.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
