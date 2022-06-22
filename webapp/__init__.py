from config import Config
from flask import Flask, current_app, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

from webapp.models import Buildings
from webapp.forms import RentFilterForm
from webapp.sections.views import search_sections


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    @app.route('/', methods=['GET', 'POST'])
    def main():
        yandex_api = current_app.config['YANDEX_API_KEY_MAP']
        rent_form = RentFilterForm() 
               
        buildings_data = Buildings.query.all()
        sections = search_sections(rent_form)

        return render_template('main.html', yandex_api=yandex_api, form_1=rent_form, \
            buildings_data=buildings_data, \
            sections=sections)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page404.html'), 404


    return app
