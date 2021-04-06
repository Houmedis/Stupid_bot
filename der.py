import os

from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, login_required, current_user
from flask_login import logout_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from data import db_session
from data.users import User
from data.job import Jobs
from data.weather import Weather


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key


class LoginForm(FlaskForm):
    name = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?')
    submit = SubmitField('Submit')
    

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() 
    return render_template('login.html', title='Авторизация', form=form, 
                           message='0')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
