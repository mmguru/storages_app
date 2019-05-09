from datetime import datetime
from storages import db, bcrypt, login_manager, app
from flask_login import UserMixin
import secrets
from flask_script import Manager
#
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(60))
    address = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip = db.Column(db.String(5))
    units = db.relationship('StorageUnit', backref='customer')
    invoices = db.relationship('Invoice', backref='customer')

class StorageUnit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit_number = db.Column(db.String)
    date_rented = db.Column(db.DateTime)
    date_vacated = db.Column(db.DateTime)
    available = db.Column(db.Boolean, default=False)
    monthly_price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    invoices = db.relationship('Invoice', backref='unit')

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    storage_id = db.Column(db.Integer, db.ForeignKey('storage_unit.id'))
    invoice_date = db.Column(db.DateTime)
    invoice_due_date = db.Column(db.Date)
    tax_rate = db.Column(db.Integer(2))
    ammount_due = db.Column(db.Integer)
    paid = db.Column(db.Boolean, nullable=False, default=False)

#
##
