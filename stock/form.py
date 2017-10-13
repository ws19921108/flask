#-*-coding:utf-8-*-

from flask_wtf  import FlaskForm
from wtforms import SubmitField, StringField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    login = SubmitField('Login')

class UploadForm1(FlaskForm):
    upFile = FileField('图片', validators=[DataRequired()])
    submit1 = SubmitField('上传')

class UploadForm2(FlaskForm):
    upFile = FileField('图片', validators=[DataRequired()])
    submit2 = SubmitField('上传')

class CompareForm(FlaskForm):
    submitCompare = SubmitField('比对')

