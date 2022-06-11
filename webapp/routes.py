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
def buildings():
    building = session.query(Buildings).all()
    return render_template('show_buldings.html', building=building)

@app.route("/buildings/<int:id>")
def building_sections(id):
    tenants = session.query(Sections).filter_by(tenant_id=id).all()
    sections = session.query(Sections).filter_by(building_id=id).all()
    return render_template('show_sections.html',sections=sections,tenants=tenants)

#@app.route("/tenants")
#def tenants_in_section():
    #tenants = session.query(Tenants).all()
    #return render_template('show_tenants.html',tenants=tenants)
       
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404

    
