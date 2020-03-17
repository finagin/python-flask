import json
import os
import psycopg2
import sqlite3
from flask import Flask, escape, request, send_file

app = Flask(__name__)

table = 'requests'

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')

try:
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {table} (data text, args text)")
    conn.commit()
except:
    print('error')


@app.route('/', methods=['GET', 'POST'])
def hello():
    try:
        cursor = conn.cursor()
        data = [
            (
                request.data,
                json.dumps(request.args),
            ),
        ]

        cursor.executemany(f"INSERT INTO {table} VALUES (?, ?)", data)
        conn.commit()
    except:
        print('Can\'t insert into "%s"')

    return json.dumps({
        'data': request.data,
        'args': request.args,
    })

#
# @app.route('/data')
# def data():
#     requests = db.query(f"select * from {table}")
#
#     return json.dumps(requests)
