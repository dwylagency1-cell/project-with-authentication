from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.secret_key = "some_key"

    db.init_app(app)

    
    login_manager.init_app(app)

    from blueprint_2.signup.models import user
    @login_manager.user_loader
    def load_user(uid):
        return user.query.get(uid)
        

    
    bcrypt.init_app(app)


    migrate = Migrate(app,db)

    return app