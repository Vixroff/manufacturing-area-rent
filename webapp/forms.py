from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length, InputRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class RentFilterForm(FlaskForm):
    func = SelectField('Выбирете назначение помещения - ', choices=[('Офис', 'Офис' ), ('Производство', 'Производство'), ('Склад', 'Склад')])
    area_min = IntegerField('Минимальная площадь кв м' , validators=[DataRequired(), NumberRange(min=0, message='Число не может быть меньше 0') ])
    area_max = IntegerField('Максимальная площадь кв м' , validators=[DataRequired(), NumberRange(min=0, message='Число не может быть меньше 0')])
    submit = SubmitField('Применить фильр')


class ContactForm(FlaskForm):
    name_cmpany = StringField('Компания', validators=[DataRequired(), Length(min=2, max=30, message="Поле не может иметь меньше 2х и больше 30ти символов")])
    name = StringField('Как мы можем к Вам обращаться', validators=[DataRequired(), Length(min=2, max=10, message="Поле не может иметь меньше 2х и больше 10ти символов")])
    email = EmailField("Email",  validators=[InputRequired("Пожалуйста введите адрес электронной почты"), Email("Пожалуйста введите адрес электронной почты")])
    phone = StringField('Контактный номер',validators=[DataRequired()])
    message = TextAreaField('Задать вопрос', validators=[DataRequired(), Length(min=1, max=250)]) 
    submit3 = SubmitField('Отправить')