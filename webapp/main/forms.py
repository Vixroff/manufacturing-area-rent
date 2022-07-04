from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, StringField, ValidationError
from wtforms.validators import DataRequired, NumberRange, InputRequired


def check_area(form, field):
    if field.data < form.area_min.data:
        raise ValidationError('Максимальная площадь должна больше минимальной')

class FindSection(FlaskForm):
    func = SelectField('Выбирете назначение помещения - ',
                choices=[('Офис', 'Офис' ), ('Производство', 'Производство'), ('Склад', 'Склад')])
    area_min = IntegerField('Минимальная площадь, м²', default=0,
                validators=[InputRequired(), NumberRange(min=0, message='Число не может быть меньше 0')])
    area_max = IntegerField('Максимальная площадь, м²', 
                validators=[InputRequired(), NumberRange(min=0, message='Число не может быть меньше 0'), check_area])
    submit1 = SubmitField('применить')
    


class FindTenant(FlaskForm):
    name = StringField(id='autocomplete', validators=[DataRequired()], \
        render_kw={"placeholder": "  Поиск"})
    submit2 = SubmitField('Найти')
