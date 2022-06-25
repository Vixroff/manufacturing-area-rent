from webapp import app, db
from config import Config
from flask import render_template,  request,  url_for, json, flash
from TG_bot import message_bot, chat_id


from webapp.models import Buildings, Tenants, Sections
from webapp.forms import RentFilterForm, LoginForm, ContactForm



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
        if form.validate_on_submit and form.area_min.data <= form.area_max.data:
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
            flash('Некорректно введены данные.', category='error')
            return render_template('rent_sections.html',form=form)
    else:
        return render_template('rent_sections.html', form=form, result=result)


@app.route("/tenants/")
def tenants():
    tenants = Tenants.query.all()
    return render_template('tenants_list.html', tenants=tenants)


@app.route('/contact/', methods=['GET', 'POST']) 
def contact_form():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            message_to_tgBot = (f'Компания: {form.name_cmpany.data}\n'
                                f'Имя: {form.name.data}\n'
                                f'Почта: {form.email.data}\n'
                                f'Телефон: {form.phone.data}\n'
                                f'Сообщение: {form.message.data}\n')
            message_bot.send_message(chat_id, message_to_tgBot, disable_notification = True)
            flash('Спасибо! Мы обязательно свяжимся с вами!', category='succes')
            return render_template('contact_form.html',form=form)
    else:
        return render_template('contact_form.html',form=form)
    
   
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404


@app.route('/map')
def get_map():
    buildings = Buildings.query.all()
    return render_template('map.html', title= 'Map', buildings = buildings)

