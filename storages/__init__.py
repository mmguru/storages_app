from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from datetime import datetime


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand




app = Flask(__name__)
app.config['SECRET_KEY'] = ''

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# from .core.views import core
# from .users.views import users
#
# app.register_blueprint(core)
# app.register_blueprint(users)

# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))



#
# if __name__ == '__main__':
#     manager.run()
