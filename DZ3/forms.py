from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])

    password = PasswordField('Пароль', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_pas = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])