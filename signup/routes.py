from flask import redirect, request, render_template, Blueprint, url_for
from flask_login import login_user, logout_user
from blueprint_2.signup.models import User
from blueprint_2.app2 import bcrypt
from blueprint_2.app2 import db

signup = Blueprint("signup",__name__, template_folder="templates")

@signup.route("/signup", methods= ["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup/signup.html")
    
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hash_password = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(username=username, password=hash_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("dashboard.dash"))