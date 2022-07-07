from flask import Blueprint, current_app, flash, jsonify, render_template, request

from webapp.Message_to_Telegram import chat_id, send_message_to_telegram, token
from webapp.main.forms import ContactForm, FindSection, FindTenant
from webapp.main.get_sections import search_sections
from webapp.main.models import Buildings, Tenants

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def main():
    yandex_api = current_app.config['YANDEX_API_KEY_MAP']
    find_section_form = FindSection()
    find_tenant_form = FindTenant()
    buildings_data = Buildings.query.all()
    contact_form = ContactForm()
    sections = None
    if request.method == 'POST' and find_section_form.submit1.data:
        if find_section_form.validate():
            func = find_section_form.func.data
            area_min = find_section_form.area_min.data
            area_max = find_section_form.area_max.data
            sections = search_sections(func, area_min, area_max)
        for _, error in find_section_form.errors.items():
            flash(error)
        if not sections:
            flash('Нет свободных помещений по вашему запросу, пожалуйста, свяжитесь с нами, и мы поможем Вам.',
                  category='error')
    tenant = None
    if request.method == 'POST' and find_tenant_form.submit2.data:
        tenant = Tenants.query.filter(Tenants.name == find_tenant_form.name_tenant.data).first()
    if request.method == 'POST' and contact_form.submit3.data:
        if contact_form.validate():
            callback_application = (f'Компания: {contact_form.name_company.data}\n'
                                    f'Имя: {contact_form.name_user.data}\n'
                                    f'Почта: {contact_form.email.data}\n'
                                    f'Телефон: {contact_form.phone.data}\n'
                                    f'Сообщение: {contact_form.message.data}\n')
            send_message_to_telegram(token, chat_id, callback_application)
    return render_template(
        'main.html', yandex_api=yandex_api,
        section_form=find_section_form, tenant_form=find_tenant_form,
        buildings_data=buildings_data,
        sections=sections, tenant=tenant, contact_form=contact_form,
    )


@bp.route('/autocomplete', methods=['GET'])
def autocomplete():
    tenants_data = [tenant.name for tenant in Tenants.query.all()]
    return jsonify(json_list=tenants_data)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404
