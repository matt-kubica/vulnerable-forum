from flask import Blueprint, render_template, request


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'GET':
        return render_template('questions.html', questions=['aaaa', 'bbb', 'ccc'])

    session_id = request.cookies.get('session_id')
    from .auth import cookies
    from .database import add_question
    if session_id in cookies:
        username = cookies[session_id]
        question = request.form.get('question')
        add_question(username, question)
        return render_template('questions.html')
    return render_template('questions.html')
