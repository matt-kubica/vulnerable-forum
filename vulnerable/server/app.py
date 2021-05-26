from flask import Flask, render_template, request
from flask.wrappers import Request
import os
import helper_functions.testDB as helperFunctions

app = Flask(__name__, template_folder="front_end/templates")

@app.route('/')
def hello_world():
    db()
    return 'Hello, World!'

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        helperFunctions.db()
        return helperFunctions.hello()
    else:
        return render_template('questions.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')