from flask import Blueprint, render_template, redirect, url_for, request, flash

from .models import User
from . import db
import logging, uuid, functools

logging.basicConfig(level=logging.DEBUG)
auth = Blueprint('auth', __name__)

# uuid -> User
cookies = {

}

def generate_cookie(user):
    generated_uuid = str(uuid.uuid4())
    cookies[generated_uuid] = user
    return generated_uuid

@auth.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    # validate if fields have been provided
    if username and password:
        # check if user exist
        user = User.query.filter_by(username=username).first()
        # 'authenticate' user
        if not user or not user.password == password:
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        res = redirect(url_for('main.questions'))
        session_id = generate_cookie(user)
        res.set_cookie('session_id', session_id)
        return res
    else:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))



@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'GET':
        return render_template('signup.html')

    # grab data from the form
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    # validate if fields have been provided
    if email and username and password:
        # if user doesn't exist yet, can be added to database
        if not User.query.filter_by(username=username, email=email).first():
            user = User(username=username, email=email, password=password)
            logging.debug(user)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
    else:
        flash('Credentials not provided')
        return render_template('signup.html')


@auth.route('/logout')
def logout():
    session_id = request.cookies.get('session_id')
    if session_id in cookies: del cookies[session_id]
    return redirect(url_for('auth.login'))
