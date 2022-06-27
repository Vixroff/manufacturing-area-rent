from flask import flash, session
from webapp.models import Sections


def search_sections(func, area_min, area_max):         
    sections = Sections.query.order_by(Sections.building_id) \
        .filter(Sections.function == func) \
        .filter(area_max >= Sections.area, Sections.area >= area_min) \
        .filter(Sections.tenant_id.is_(None)) \
        .all()
    if not sections:
        flash('Нет свободных помещений по вашему запросу, пожалуйста, свяжитесь с нами, и мы поможем Вам с выбором.', 
        category='error')
        return 
    return sections