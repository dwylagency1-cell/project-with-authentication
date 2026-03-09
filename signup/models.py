from flask_login import UserMixin
from blueprint_2.app2 import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return f"Username: {self.username} password: {self.password}"
    
    def get_id(self):
        return str(self.uid)