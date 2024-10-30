from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.page import page
    from .routes.auth import auth

    app.register_blueprint(page)
    app.register_blueprint(auth)

    return app
