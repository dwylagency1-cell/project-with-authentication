from flask import redirect, url_for, Blueprint, render_template

dashboard = Blueprint("dashboard", __name__, template_folder='templates')

@dashboard.route("/dashboard")
def dash():
    return render_template("dashboard.html")