from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = TextAreaField("Name Of Student", [validators.DataRequired("Please enter your name")])
    gender = RadioField("Gender", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")])
    address = TextAreaField("Address")
    email = TextAreaField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address in the correct format.")])
    age = IntegerField("Age")
    language = SelectField("Language", choices=[("cpp", "C++"), ("py", "Python")])
    submit = SubmitField("Send")
