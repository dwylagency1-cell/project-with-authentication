from flask import redirect, url_for, Blueprint, render_template, request
from blueprint_2.app2 import login_manager
from blueprint_2.app2 import bcrypt
from blueprint_2.app2 import db

login = Blueprint("login", __name__, template_folder="templates")

@login.route("/login" , methods = ["GET", "POST"])
def log_in():
    if request.method == 'GET':
        return render_template("login.html")
    
    elif request.method == 'POST':
        password = request.form.get("password")
        username = request.form.get("username")
        


