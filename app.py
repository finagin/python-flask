import json
import os
import psycopg2
import sqlite3
from flask import Flask, escape, request, send_file

app = Flask(__name__)

table = 'requests'

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
#
# try:
#     cursor = conn.cursor()
#
#     try:
#         cursor.execute(f"CREATE TABLE {table} (data text, args text)")
#     except Exception as e:
#         cursor.close()
#     else:
#         conn.commit()
# except:
#     print('error')


@app.route('/', methods=['GET', 'POST'])
def hello():
    # try:
    cursor = conn.cursor()
    data = [
        (
            json.dumps(request.data),
            json.dumps(request.args if request.args else None),
        ),
    ]

    cursor.executemany(f"INSERT INTO {table} VALUES (%s, %s)", data)
    conn.commit()
    # except SyntaxError as e:
    #     print(f'Can\'t insert into {type(e).__name__}"')

    return json.dumps({
        'status': 'Ok',
    })

#
# @app.route('/data')
# def data():
#     requests = db.query(f"select * from {table}")
#
#     return json.dumps(requests)
