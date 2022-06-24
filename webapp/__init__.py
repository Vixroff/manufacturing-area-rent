from config import Config
from flask import Flask, current_app, redirect, render_template, request, jsonify, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from webapp.models import Buildings, Tenants
from webapp.forms import FindSection, FindTenant
from webapp.sections.views import search_sections


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    @app.route('/', methods=['GET', 'POST'])
    def main():
        yandex_api = current_app.config['YANDEX_API_KEY_MAP']
        find_section_form = FindSection()
        find_tenant_form = FindTenant()
        buildings_data = Buildings.query.all()


        if request.method == 'POST' and find_section_form.submit1.data:
                session['func'] = find_section_form.func.data
                session['area_min'] = find_section_form.area_min.data
                session['area_max'] = find_section_form.area_max.data
                print('a')
                return redirect(url_for('main'))
        if session.get('func') and session.get('area_min') and session.get('area_max'):
            print(session.get('func'), session.get('area_min'), session.get('area_max'))
            sections = search_sections(session.get('func'), session.get('area_min'), session.get('area_max'))
        else:
            print('b')
            sections = None


        if session.get('tenant'):
            tenant = Tenants.query.filter(Tenants.name==session.get('tenant')).first()
        else:
            tenant = None
        if request.method == 'POST' and find_tenant_form.submit2.data:
            session['tenant'] = find_tenant_form.name.data
            return redirect(url_for('main'))

           
        return render_template('main.html', yandex_api=yandex_api, \
            form_1=find_section_form, form_2=find_tenant_form, \
            buildings_data=buildings_data, \
            sections=sections, tenant=tenant)


    @app.route('/autocomplete',methods=['GET'])
    def autocomplete():
        tenants_data = [tenant.name for tenant in Tenants.query.all()]
        return jsonify(json_list=tenants_data)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page404.html'), 404


    return app
