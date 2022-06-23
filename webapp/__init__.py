from config import Config
from flask import Flask, current_app, render_template, request, jsonify
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
            sections = search_sections(find_section_form)
        else:
            sections = None

        if request.method == 'POST' and find_tenant_form.submit2.data:
            tenant = Tenants.query.filter(Tenants.name==find_tenant_form.name.data).first()
            
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
