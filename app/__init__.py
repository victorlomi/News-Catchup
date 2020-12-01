from flask import Flask, request, current_app
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.source import bp as source_bp
    app.register_blueprint(source_bp)

    return app

