import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .models.base import Base

db = SQLAlchemy(model_class=Base)


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB__ENGINE"]

    db.init_app(app)

    from .routes.page import page
    from .routes.auth import auth

    app.register_blueprint(page)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
