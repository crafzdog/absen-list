from flask import Blueprint, render_template

page = Blueprint("page", __name__)


@page.route("/")
def home_page():
    return render_template("index.html")


@page.route("/features")
def features_page():
    return "Features page"
