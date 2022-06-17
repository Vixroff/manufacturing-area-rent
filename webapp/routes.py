from webapp import app, db
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


@app.route("/buildings/<int:building_id>")
def building_sections(building_id):
    sections = db.session.query(Sections).filter_by(building_id=str(building_id)).all()
    return render_template('show_sections.html',sections=sections)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404


@app.route('/map')
def get_map():
    buildings = Buildings.query.all()
    return render_template('map.html', title= 'Map', buildings = buildings)

