import json
import os
import psycopg2
import sqlite3
from flask import Flask, escape, request, send_file

app = Flask(__name__)

table = 'requests'

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')

try:
    conn.execute(f"CREATE TABLE {table} (data text, args text)")
except:
    print('error')


@app.route('/', methods=['GET', 'POST'])
def hello():
    # ins = db.prepare(f"INSERT INTO {table} VALUES ($1, $2)")

    # try:
    # ins(
    #     request.data,
    #     json.dumps(request.args)
    # )
    # except:
    #     logger.warning('Can\'t json dump', extra=d)
    #     logger.warning('Can\'t insert into "%s"', table, extra=d)

    return json.dumps({
        'status': 'Ok',
    })

#
# @app.route('/data')
# def data():
#     requests = db.query(f"select * from {table}")
#
#     return json.dumps(requests)
