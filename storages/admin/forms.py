from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from webapp.models import User
from wtforms.fields.html5 import DateField, TimeField

class addNewCustomer(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    phone_number = StringField('Phone Number')
    address = StringField('Address')
    address2 = StringField()
    city = StringField('City')
    state = StringField('State')
    zip = StringField('zip')
    submit = SubmitField("Add Customer")

class addNewStorageUnit(FlaskForm):
    unit_number = StringField("Unit Number/Name")
    monthly_price = IntegerField("Price Per Month")
    late_fee = IntegerField("Late Fee")
    submit = SubmitField("Add Unit")
