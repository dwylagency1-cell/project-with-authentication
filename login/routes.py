from flask import redirect, url_for, Blueprint, render_template, request
from flask_login import login_user, logout_user
from blueprint_2.app2 import bcrypt
from blueprint_2.app2 import db
from blueprint_2.signup.models import User

login = Blueprint("login", __name__, template_folder="templates")

@login.route("/login" , methods = ["GET", "POST"])
def log_in():
    if request.method == 'GET':
        return render_template("login/login.html")
    
    elif request.method == 'POST':
        password = request.form.get("password")
        username = request.form.get("username")

        user = User.query.filter(User.username == username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard.dash"))
        else:
            return "Invalid username or password"

        
        


