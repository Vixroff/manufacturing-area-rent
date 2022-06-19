from webapp import app, db
from config import Config
from flask import render_template, redirect, request, session, url_for, json, flash


from webapp.models import Buildings, Tenants, Sections
from webapp.forms import RentFilterForm, LoginForm



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

@app.route("/rent/", methods=['GET', 'POST'])
def rent():
    form = RentFilterForm()
    result = Sections.query.filter(Sections.tenant_id.is_(None)).all()
    if request.method == 'POST':
        if form.validate_on_submit:
            result = Sections.query.order_by(Sections.building_id) \
                .filter(Sections.function == form.func.data) \
                .filter(form.area_max.data >= Sections.area, Sections.area >= form.area_min.data) \
                .filter(Sections.tenant_id.is_(None)) \
                .all()
            if not result:
                flash('Нет свободных помещений по вашему запросу, пожалуйста, свяжитесь с нами, и мы поможем Вам с выбором.', category='error')
                return render_template('rent_sections.html',form=form)
            else:
                return render_template('rent_sections.html',form=form, result=result)
    else:
        return render_template('rent_sections.html', form=form, result=result)
    

@app.route("/tenants/")
def tenants():
    tenants = Tenants.query.all()
    return render_template('tenants_list.html', tenants=tenants)

    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404


@app.route('/map')
def get_map():
    buildings = Buildings.query.all()
    return render_template('map.html', title= 'Map', buildings = buildings)

