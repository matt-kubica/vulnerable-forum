from flask import Flask
import psycopg2
import os

app = Flask(__name__)


def db():
    # con = psycopg2.connect(database=os.environ.get('POTGRES_DB'),
    #                        user=os.environ.get('POSTGRES_USER'), 
    #                        password=os.environ.get('POSTGRES_PASSWORD'), 
    #                        host="db", port="5432")
    con = psycopg2.connect(database='default',
                           user='admin', 
                           password='admin', 
                           host="db", port="5432")
    print("Database opened successfully")

    cur = con.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES ('John', 'some-hash')");

    con.commit()
    print("Record inserted successfully")
    con.close()



@app.route('/')
def hello_world():
    db()
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')