from flask import Blueprint, render_template, request
from .database import get_questions, get_questionID, insertAnswer, get_userID, add_question
from .helper_functions import getSecondIndexes, getUsernameFromSessionID
import logging

logging.basicConfig(level=logging.DEBUG)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'GET':
        # getSecondIndexes is used to flatten the 2d array we get from db query
        return render_template('questions.html', questions=getSecondIndexes(get_questions()))

    username = getUsernameFromSessionID(request.cookies.get('session_id'))
    if username:
        add_question(username, request.form.get('question'))
        return render_template('questions.html', questions=getSecondIndexes(get_questions()))
    return render_template('questions.html', questions=getSecondIndexes(get_questions()))

@main.route('/answers', methods=['GET', 'POST'])
def answers():
    if request.method == 'POST':
        username_ = getUsernameFromSessionID(request.cookies.get('session_id'))
        if username_:
            insertAnswer(questionID = get_questionID(question = request.form.get('question')), userID = get_userID(username = username_) , answer = request.form.get('answer'))
            return render_template('questions.html', questions=getSecondIndexes(get_questions()), resStatus = "Your answer has been submitted")
    return render_template('questions.html', questions=getSecondIndexes(get_questions()), resStatus = "You need to login in order to answer questions")
