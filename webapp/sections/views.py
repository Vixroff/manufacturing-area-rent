from flask import flash, request
from webapp.models import Sections


def search_sections(form):        
    if form.validate_on_submit and form.area_min.data <= form.area_max.data:
        sections = Sections.query.order_by(Sections.building_id) \
            .filter(Sections.function == form.func.data) \
            .filter(form.area_max.data >= Sections.area, Sections.area >= form.area_min.data) \
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