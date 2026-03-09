from flask import render_template, redirect, url_for, Blueprint

home = Blueprint("home", __name__, template_folder="templates")

@home.routes("/")
def home_page():
    return render_template("home.html")
