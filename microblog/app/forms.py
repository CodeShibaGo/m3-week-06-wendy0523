from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    username = StringField('使用者名', validators=[DataRequired(message="用戶名不可空白或超過32字")])
    password = PasswordField('密碼', validators=[DataRequired(message="密碼不可空白"), Length(min=6, max=32, message="密碼長度應為6到32個字符")])
    remember_me = BooleanField('記住我')
    submit = SubmitField('登入')