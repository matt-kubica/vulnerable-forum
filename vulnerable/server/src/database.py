import psycopg2
import logging, os

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
    logging.debug('Added user to database...')


def add_question(username, question):
    cur = connection.cursor()
    cur.execute("SELECT id FROM users WHERE username='{0}';".format(username))
    res = cur.fetchall()
    if len(res) > 0:
        user_id = res[0][0]
        cur.execute("INSERT INTO questions (user_id, question_text) VALUES ('{0}', '{1}');".format(user_id, question))
        connection.commit()
        logging.debug('Added question to database...')

def get_user(**kwargs):
    cur = connection.cursor()

    if 'email' in kwargs and 'username' in kwargs:
        cur.execute("SELECT * FROM users WHERE email='{0}' AND username='{1}';"
                    .format(kwargs['username'], kwargs['email']))
        res = cur.fetchall()
        return res[0] if len(res) > 0 else None

    if 'username' in kwargs:
        cur.execute("SELECT * FROM users WHERE username='{0}';".format(kwargs['username']))
        res = cur.fetchall()
        return res[0] if len(res) > 0 else None

    return None


