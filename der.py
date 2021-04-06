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
from data.form import *
from data.weather import Weather


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
user = None
sl = {}


@login_manager.user_loader
def load_user(user_id):
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        db_session.global_init("db/mars.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.name.data).first()
        if user is not None:
            if user.hashed_password == form.password.data:
                global sl
                sl = {}
                login_user(user, remember=form.remember_me.data)
                sl['email'] = user.email
                sl['name'] = user.name
                sl['weather'] = user.weather
                sl['chat'] = user.chat
                id = user.id
                return redirect(f"/enter/{id}")
        else:
            return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)    
    return render_template('login.html', title='Авторизация', form=form, 
                           message='0')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)