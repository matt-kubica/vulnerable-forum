from flask import Blueprint, render_template, request, flash

from .database import add_answer, add_question, add_user
from .database import get_questions, get_question, get_answers
from .helper_functions import get_user_from_session_id
import logging

logging.basicConfig(level=logging.DEBUG)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user = get_user_from_session_id(request.cookies.get('session_id'))
    return render_template('index.html', username=user.username if user else 'guest')

@main.route('/questions', methods=['GET', 'POST'])
def questions():
    # render page in case of get request
    if request.method == 'GET':
        return render_template('questions.html', questions=get_questions())

    # handle post request in other case
    user = get_user_from_session_id(request.cookies.get('session_id'))
    # if user is logged in, question can be added, template eis rendered with new question
    if user:
        add_question(user_id=user.id, question_text=request.form.get('question'))
        return render_template('questions.html', questions=get_questions())
    # otherwise error message is flashed
    flash('You need to login in order to ask a question')
    return render_template('questions.html', questions=get_questions())


@main.route('/answers/<question_id>')
def answers_get(question_id):
    question = get_question(id=question_id)
    answers = get_answers(question_id=question_id)
    return render_template('answers.html', question=question, answers=answers)


@main.route('/answers', methods=['POST'])
def answers_post():
    question_id = request.form.get('question_id')
    user = get_user_from_session_id(request.cookies.get('session_id'))
    question = get_question(id=question_id)

    if user:
        add_answer(question_id=question_id,
                   user_id=user.id,
                   answer_text=request.form.get('answer'))
        return render_template('answers.html', question=question, answers=get_answers(question_id=question_id))

    flash('You need to login in order to answer a question')
    return render_template('answers.html', question=question, answers=get_answers(question_id=question_id))