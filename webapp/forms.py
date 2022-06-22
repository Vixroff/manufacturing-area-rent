from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange

    
class RentFilterForm(FlaskForm):
    func = SelectField('Выбирете назначение помещения - ', choices=[('Офис', 'Офис' ), ('Производство', 'Производство'), ('Склад', 'Склад')])
    area_min = IntegerField('Минимальная площадь кв м' , validators=[DataRequired(), NumberRange(min=0, message='Число не может быть меньше 0') ])
    area_max = IntegerField('Максимальная площадь кв м' , validators=[DataRequired(), NumberRange(min=0, message='Число не может быть меньше 0')])
    submit = SubmitField('Применить фильтр')
