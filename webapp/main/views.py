from flask import Blueprint, current_app, render_template, request, jsonify, flash

from webapp import create_app
from webapp.main.models import Buildings, Tenants
from webapp.main.forms import FindSection, FindTenant
from webapp.main.get_sections import search_sections

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def main():
    yandex_api = current_app.config['YANDEX_API_KEY_MAP']
    find_section_form = FindSection()
    find_tenant_form = FindTenant()
    buildings_data = Buildings.query.all()

    sections = None
    if request.method == 'POST' and find_section_form.submit1.data:
        if find_section_form.validate():
            func = find_section_form.func.data
            area_min = find_section_form.area_min.data
            area_max = find_section_form.area_max.data
            sections = search_sections(func, area_min, area_max)
        for _, error in find_section_form.errors.items():
            flash(error)

    tenant = None
    if request.method == 'POST' and find_tenant_form.submit2.data:
        tenant = Tenants.query.filter(Tenants.name==find_tenant_form.name.data).first()

        
    return render_template('main.html', yandex_api=yandex_api, \
        section_form=find_section_form, tenant_form=find_tenant_form, \
        buildings_data=buildings_data, \
        sections=sections, tenant=tenant)


@bp.route('/autocomplete',methods=['GET'])
def autocomplete():
    tenants_data = [tenant.name for tenant in Tenants.query.all()]
    return jsonify(json_list=tenants_data)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404