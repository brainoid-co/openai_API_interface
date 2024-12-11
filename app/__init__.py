from flask import Flask
from config import Config
from .database import db
from .models import ChatHistory, SessionData

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

    from .routes import main
    app.register_blueprint(main)

    return app
