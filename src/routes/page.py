from flask import Blueprint, render_template

page = Blueprint("page", __name__)


@page.route("/")
def home_page():
    return render_template("index.jinja2")


@page.route("/features")
def features_page():
    return render_template("features.jinja2")


@page.route("/about")
def about_page():
    return render_template("about.jinja2")


@page.route("/contact")
def contact_page():
    return render_template("contact.jinja2")

@page.route("/test")
def test_page():
    return render_template("test.jinja2")