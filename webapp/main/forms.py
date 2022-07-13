from flask_wtf import FlaskForm

from wtforms import EmailField, IntegerField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, InputRequired, Length, NumberRange


def check_area(form, field):
    if field.data < form.area_min.data:
        raise ValidationError('Максимальная площадь должна больше минимальной')


class FindSection(FlaskForm):
    func = SelectField(
        'Выбирете назначение помещения - ',
        choices=[('Офис', 'Офис'), ('Производство', 'Производство'), ('Склад', 'Склад')],
    )
    area_min = IntegerField(
        'Минимальная площадь, м²', default=0,
        validators=[InputRequired(),
                    NumberRange(min=0, message='Число не может быть меньше 0')],
    )
    area_max = IntegerField(
        'Максимальная площадь, м²', default=0,
        validators=[InputRequired(),
                    NumberRange(min=0, message='Число не может быть меньше 0'), check_area],
    )
    submit1 = SubmitField('применить')


class FindTenant(FlaskForm):
    name_tenant = StringField(
        'Название компании', id='autocomplete', validators=[DataRequired()], render_kw={"placeholder": "  Поиск"})
    submit2 = SubmitField('Найти')


class ContactForm(FlaskForm):
    name_company = StringField(
        'Компания',
        validators=[DataRequired(),
                    Length(min=2, max=30, message="Поле не может иметь меньше 2х и больше 30ти символов")],
        render_kw={"placeholder": "  Название компании"},
    )
    name_user = StringField(
        'Как мы можем к Вам обращаться',
        validators=[DataRequired(),
                    Length(min=2, max=10, message="Поле не может иметь меньше 2х и больше 10ти символов")],
        render_kw={"placeholder": "  Ф.И.О."},
    )
    email = EmailField(
        "Email",
        validators=[InputRequired("Пожалуйста введите адрес электронной почты"),
                    Email("Пожалуйста введите адрес электронной почты")],
        render_kw={"placeholder": "  Email"},
    )
    phone = StringField(
        'Контактный номер',
        validators=[DataRequired()],
        render_kw={"placeholder": "  Номер телефона"},
    )
    message = StringField(
        'Задать вопрос',
        validators=[DataRequired(),
                    Length(min=1, max=250)],
        render_kw={"placeholder": "  Оставить сообщение"},
    )
    submit3 = SubmitField('Отправить')
