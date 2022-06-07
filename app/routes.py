from flask import render_template, redirect, request, session, url_for
from app import app
from app.forms import LoginForm


@app.route('/index')
@app.route("/")
def index():
    return render_template('main_page.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login_page.html', title='Sign In', form=form)