from flask import Flask
from .models import db
import os

app = Flask(__name__)

db_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), os.path.relpath("db/database.db")
)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

db.init_app(app)

from .routes.page import page
from .routes.auth import auth

app.register_blueprint(page)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()
