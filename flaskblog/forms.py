from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# check user exist or not - import User model 
from flaskblog.models import User

# create a registration form class
# class representative of form , and then converted to html form - inherit form FlaskForm
# form field are all imported class
# ex: user name is a string field

class RegistrationForm(FlaskForm):
    # we don't want the filed to be empty or too long name
    # use validator, the validation are also class import (example: datarequired, length)
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators =[DataRequired()])
    # comfirmed password is equal to the password field
    comfirmed_password = PasswordField('Confirm Password', 
                                        validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # custom validation
    # to prevent ugly database integrity error occur
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            # wtforms.validators
            raise ValidationError('The username is already taken. Please choose a different one.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            # wtforms.validators
            raise ValidationError('The email is already taken. Please choose a different one.')

class LoginForm(FlaskForm):
    
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators =[DataRequired()])
    # secure cookie
    remember =BooleanField('Remember Me')
    submit = SubmitField('Login')