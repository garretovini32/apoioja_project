from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

# Inicialização do banco e migração
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, static_folder="static", template_folder="templates")
    
    # Configurações básicas
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('FLASK_SECRET', 'devkey'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', 'sqlite:///app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Importa rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
