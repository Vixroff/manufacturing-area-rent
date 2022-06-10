from flask import render_template, redirect, request, session, url_for
from webapp import app
from webapp.login_forms import LoginForm
from model import Buildings, Tenants, Sections
from db import db_session
session = db_session


@app.route('/index')
@app.route("/")
def index():
    return render_template('main_page.html', title= 'Главная страница')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login_page.html', title='Sign In', form=form)

@app.route("/buildings")
def show_buildings():
    building = session.query(Buildings).all()
    return render_template('show_buldings.html', building=building)

@app.route("/sections")
def show_sections():
    buildings_id = session.query(Buildings.id).all()
    sectionss = session.query(Sections).all()
    return render_template('show_sections.html',sectionss=sectionss,buildings_id=buildings_id)


