# project/users/forms.py

# Docs: https://wtforms.readthedocs.io/en/3.0.x/

from flask_wtf import FlaskForm
# from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Optional, Length, EqualTo, Email
# Email validator needs add-on package: pip install wtforms[email]



class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    



class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])