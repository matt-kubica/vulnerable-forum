from flask import Blueprint, render_template, request, flash

from .helper_functions import get_user_from_session_id
from .models import Question, User, Answer
from . import db
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
        return render_template('questions.html', questions=Question.query.all())

    # handle post request in other case
    user = get_user_from_session_id(request.cookies.get('session_id'))
    # if user is logged in, question can be added, template eis rendered with new question
    if user:
        question = Question(user_id=user.id, question_text=request.form.get('question'))
        db.session.add(question)
        db.session.commit()
        return render_template('questions.html', questions=Question.query.all())
    # otherwise error message is flashed
    flash('You need to login in order to ask a question')
    return render_template('questions.html', questions=Question.query.all())


@main.route('/answers/<question_id>')
def answers_get(question_id):
    question = Question.query.filter_by(id=question_id).first()
    answers = Answer.query.filter_by(question_id=question_id).all()
    return render_template('answers.html', question=question, answers=answers)


@main.route('/answers', methods=['POST'])
def answers_post():
    question_id = request.form.get('question_id')
    user = get_user_from_session_id(request.cookies.get('session_id'))
    question = Question.query.filter_by(id=question_id).first()

    if user:
        answer = Answer(question_id=question_id, user_id=user.id, answer_text=request.form.get('answer'))
        db.session.add(answer)
        db.session.commit()
        return render_template('answers.html', question=question, answers=Answer.query.filter_by(question_id=question_id).all())

    flash('You need to login in order to answer a question')
    return render_template('answers.html', question=question, answers=Answer.query.filter_by(question_id=question_id).all())
