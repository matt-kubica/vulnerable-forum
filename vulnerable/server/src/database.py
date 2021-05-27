import psycopg2
import logging, os

from .models import User, Question, Answer

logging.basicConfig(level=logging.DEBUG)

connection_params = {
    'database': os.environ.get('POSTGRES_DB') or 'default',
    'user': os.environ.get('POSTGRES_USER') or 'admin',
    'password': os.environ.get('POSTGRES_PASSWORD') or 'admin',
    'host': 'db',
    'port': '5432',
}

connection = psycopg2.connect(**connection_params)
logging.debug('Successfully connected to database')


def add_user(email, username, password):
    cur = connection.cursor()
    cur.execute("INSERT INTO users (email, username, password) VALUES ('{0}', '{1}', '{2}');"
                .format(email, username, password))
    connection.commit()


def add_question(user_id, question_text):
    cur = connection.cursor()
    cur.execute("INSERT INTO questions (user_id, question_text) VALUES ('{0}', '{1}');"
                .format(user_id, question_text))
    connection.commit()


def add_answer(question_id, user_id, answer_text):
    cur = connection.cursor()
    cur.execute("INSERT INTO answers (question_id, user_id, answer_text) VALUES ('{0}', '{1}', '{2}');"
                .format(question_id, user_id, answer_text))
    connection.commit()


def get_user(**kwargs):
    cur = connection.cursor()

    if 'email' in kwargs and 'username' in kwargs:
        cur.execute("SELECT * FROM users WHERE email='{0}' AND username='{1}';"
                    .format(kwargs['email'], kwargs['username']))
        res = cur.fetchall()
        if res:
            return User(res[0][0], res[0][1], res[0][2], res[0][3])
        return None

    if 'username' in kwargs:
        cur.execute("SELECT * FROM users WHERE username='{0}';".format(kwargs['username']))
        res = cur.fetchall()
        if res:
            return User(res[0][0], res[0][1], res[0][2], res[0][3])
        return None


def get_userID(**kwargs):
    cur = connection.cursor()

    if 'username' in kwargs:
        cur.execute("SELECT id FROM users WHERE username='{0}';".format(kwargs['username']))
        res = cur.fetchall()
        return res[0][0] if len(res) > 0 else None

    return None



def get_questionID(**kwargs):
    cur = connection.cursor()

    if 'question' in kwargs:
        cur.execute("SELECT id FROM questions WHERE question_text='{0}';".format(kwargs['question']))
        res = cur.fetchall()
        return res[0][0] if len(res) > 0 else None
    else:
        return


def get_question(**kwargs):
    cur = connection.cursor()

    if 'id' in kwargs:
        cur.execute("SELECT * FROM questions WHERE id='{0}';".format(kwargs['id']))
        res = cur.fetchall()
        if res:
            return Question(res[0][0], res[0][1], res[0][2])
        return None


def get_questions(**kwargs):
    cur = connection.cursor()

    cur.execute("SELECT * FROM questions;")
    res = cur.fetchall()
    if res:
        return [Question(res[i][0], res[i][1], res[i][2]) for i in range(0, len(res))]
    return []


def get_answers(**kwargs):
    cur = connection.cursor()

    if 'question_id' in kwargs:
        cur.execute("SELECT * FROM answers WHERE question_id='{0}';".format(kwargs['question_id']))
        res = cur.fetchall()
        if res:
            return [Answer(res[i][0], res[i][1], res[i][2], res[i][3]) for i in range(0, len(res))]
        return []