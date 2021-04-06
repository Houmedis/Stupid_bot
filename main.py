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


@app.route('/weather/<int:id>', methods=['GET', 'POST'])
def weather(id):
    sl = Weather()
    sl_1 = {'clear': 'ясно',
          'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
          'overcast': 'пасмурно', 'drizzle': 'морось', 
          'light-rain': 'небольшой дождь',
          'rain': 'дождь', 'moderate-rain': 'умеренно сильный дождь',
          'heavy-rain': 'сильный дождь', 
          'continuous-heavy-rain': 'длительный сильный дождь',
          'showers': 'ливень', 'wet-snow': 'дождь со снегом',
          'light-snow': 'небольшой снег', 'snow-showers': 'снегопад',
          'hail': 'град', 'thunderstorm': 'гроза',
          'thunderstorm-with-rain': 'дождь с грозой', 
          'thunderstorm-with-hail': 'гроза с градом',
          }
    sl['condition'] = sl_1[sl['condition']]
    return render_template('weather.html', sl=sl, id=id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.password.data == form.rep_password.data:
            db_session.global_init("db/mars.db")
            db_sess = db_session.create_session()
            user = User()
            user.name = form.name.data
            user.email = form.job_title.data
            user.hashed_password = form.password.data
            user.weather = form.weather.data
            user.chat = form.chat.data
            db_sess.add(user)
            db_sess.commit()
            return redirect("/login")
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route('/Kirill/<int:id>', methods=['GET', 'POST'])
def Kirill(id):
    return render_template('chat_bot.html', sl=sl, id=id)


@app.route('/enter/<int:id>', methods=['GET', 'POST'])
def enterned(id):
    form = MainForm()
    global sl  
    if sl != {}:
        sl1 = sl
        db_session.global_init("db/mars.db")
        db_sess = db_session.create_session()
        return render_template('main.html', form=form, gadjet=sl, id=id)
    else:
        return redirect('/login')


@app.route('/addjob/<int:id>', methods=['GET', 'POST'])
@login_required
def addjob(id):
    form = JobForm()
    if form.validate_on_submit():
        db_session.global_init("db/mars.db")
        db_sess = db_session.create_session()
        user = Jobs()
        user.job = form.job_title.data
        user.team_leader = id
        user.work_size = form.work_size.data
        user.collaborators = form.collaborators.data
        user.is_finished = form.is_finished.data
        db_sess.add(user)
        db_sess.commit()
        return redirect(f"/enter/{id}")
    return render_template('addjob.html', form=form)


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
