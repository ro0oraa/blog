from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import data_required ,length,email,EqualTo


class RegisterationForm(FlaskForm):
    username=StringField('username',validators=[data_required(),length(min=2,max=20)])
    email=StringField('Email',validators=[data_required(),email()])
    password=PasswordField('password',validators=[data_required()])
    confirm_password=PasswordField('confirm password',validators=[data_required(),EqualTo('password')])
    submit=SubmitField('sign up')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[data_required(),email()])
    password=PasswordField('password',validators=[data_required()])
    remember=BooleanField('remember me')
    submit=SubmitField('login')    