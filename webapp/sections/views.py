from flask import flash, request
from webapp.models import Sections


def search_sections(rent_form):   
    if request.method == 'POST' and rent_form.submit.data:     
        if rent_form.validate_on_submit and rent_form.area_min.data <= rent_form.area_max.data:
            sections = Sections.query.order_by(Sections.building_id) \
                .filter(Sections.function == rent_form.func.data) \
                .filter(rent_form.area_max.data >= Sections.area, Sections.area >= rent_form.area_min.data) \
                .filter(Sections.tenant_id.is_(None)) \
                .all()
            if not sections:
                flash('Нет свободных помещений по вашему запросу, пожалуйста, свяжитесь с нами, и мы поможем Вам с выбором.', 
                category='error')
                return None
            else:
                return sections
        else:
            flash('Некорректно введены данные.', category='error')
            return None
    return None