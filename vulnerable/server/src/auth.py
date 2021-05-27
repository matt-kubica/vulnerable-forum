from flask import Blueprint, render_template, redirect, url_for, request, flash

from .database import add_user, get_user
import logging, uuid, functools

logging.basicConfig(level=logging.DEBUG)
auth = Blueprint('auth', __name__)

# uuid -> username
cookies = {

}

def generate_cookie(username):
    generated_uuid = str(uuid.uuid4())
    cookies[generated_uuid] = username
    return generated_uuid

def login_required(function):
    @functools.wraps(function)
    def decorated_function(*args, **kwargs):
        logging.debug('Decorator works')
        session_id = request.cookies.get('session_id')
        if session_id in cookies:
            logging.debug('Decorator works')
            return function(*args, **kwargs)
        raise Exception
    return decorated_function


@auth.route('/login',  methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    # validate if fields have been provided
    if username and password:
        # check if user exist
        user_credentials_array = get_user(username=username)
        # 'authenticate' user
        if not user_credentials_array or not user_credentials_array[2] == password:
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        res = redirect(url_for('main.profile'))
        # TODO: generate some random string, store it somewhere, then limit access to other pages basing on this cookie
        res.set_cookie('session_id', generate_cookie(username))
        logging.debug('cookies: {0}'.format(cookies))
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
        if not get_user(email=email, username=username):
            logging.debug('<User {0}:{1}:{2}>'.format(email, username, password))
            add_user(email=email, username=username, password=password)
            return redirect(url_for('auth.login'))
        else:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
    else:
        flash('Credentials not provided')
        return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    return 'Logout'
