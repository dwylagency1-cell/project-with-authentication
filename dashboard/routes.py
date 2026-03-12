from flask import redirect, url_for, Blueprint, render_template, request
from blueprint_2.app2 import db
from blueprint_2.dashboard.models import Notes

dashboard = Blueprint("dashboard", __name__, template_folder='templates')

@dashboard.route("/dashboard", methods = ['GET', 'POST'])
def dash():
    notes = Notes.query.all()
    return render_template("dashboard/dashboard.html", notes = notes)

@dashboard.route('/show', methods = ["GET", "POST"])
def show_page():
    title = request.form.get("title")
    content = request.form.get("content")

    new_note = Notes(title = title, content = content)

    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for("dashboard.dash"))

@dashboard.route("/delete/<pid>")
def delete(pid):
    Notes.query.filter(Notes.pid == pid).delete()

    db.session.commit()
    return redirect(url_for("dashboard.dash"))




    
