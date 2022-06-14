from webapp import app
from config import Config
from flask import render_template, redirect, request, session, url_for, json
from webapp.login_forms import LoginForm
from webapp.models import Buildings, Tenants, Sections



@app.route('/index')
@app.route("/")
def index():
    return render_template('main_page.html', title= 'Главная страница')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login_page.html', title='Sign In', form=form)


@app.route("/buildings")
def buildings():
    building = Buildings.query.all()
    return render_template('show_buldings.html', building=building)


@app.route("/buildings/<int:id>")
def building_sections(id):
    tenants = Sections.session.query.filter_by(tenant_id=id).all()
    sections = Sections.query.filter_by(building_id=id).all()
    return render_template('show_sections.html',sections=sections,tenants=tenants)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404


@app.route('/map')
def get_map():
    buildings = Buildings.query.all()
    return render_template('map.html', title= 'Map', buildings = buildings)

