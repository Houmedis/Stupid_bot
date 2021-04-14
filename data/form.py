from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, login_required, current_user
from flask_login import logout_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?')
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    job_title = StringField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rep_password = PasswordField('Repeat_Password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    weather = BooleanField('Weather')
    chat = BooleanField('Chat_bot')
    slides = BooleanField('Slides')
    submit = SubmitField('Submit')


class MainForm(FlaskForm):
    submit = SubmitField('Add work')


class WeatherForm(FlaskForm):
    name = StringField('Where are you?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SettingForm(FlaskForm):
    weather = BooleanField('Weather')
    chat = BooleanField('Chat_bot')
    slides = BooleanField('Slides')
    submit = SubmitField('Submit')


class SlidesForm(FlaskForm):
    games = BooleanField('Games')
    movies = BooleanField('Movies')
    anime = BooleanField('Anime')
    music = BooleanField('Music')
    li24 = BooleanField('Li24')
    submit = SubmitField('Submit')