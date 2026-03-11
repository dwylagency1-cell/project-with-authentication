from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///.app.db"
    app.secret_key = "some_key"

    db.init_app(app)

    from blueprint_2.home.routes import home
    from blueprint_2.signup.routes import signup
    from blueprint_2.login.routes import login
    from blueprint_2.dashboard.routes import dashboard
    from blueprint_2.logout.routes import logout

    app.register_blueprint(home)
    app.register_blueprint(signup)
    app.register_blueprint(login)
    app.register_blueprint(dashboard)
    app.register_blueprint(logout)

    
    login_manager.init_app(app)

    from blueprint_2.signup.models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
        

    
    bcrypt.init_app(app)


    migrate = Migrate(app,db)

    return app