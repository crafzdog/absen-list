from flask import Flask

app = Flask(__name__)

from .routes.page import page

app.register_blueprint(page)
