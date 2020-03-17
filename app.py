import json
import os
import postgresql
import sqlite3
from flask import Flask, escape, request, send_file

app = Flask(__name__)

table = 'requests'

db = postgresql.open(os.environ.get('DATABASE', None))

db.execute(f"CREATE TABLE {table} (data text, args text)")


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
