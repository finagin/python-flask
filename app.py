#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json
import os
import psycopg2
import sqlite3
from flask import Flask, escape, request, send_file

app = Flask(__name__)

table = 'requests'

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')


@app.route('/', methods=['GET', 'POST'])
def hello():
    cursor = conn.cursor()

    data = [
        (
            request.data.decode('utf-8'),
            json.dumps(request.args if request.args else None),
        ),
    ]

    cursor.executemany(f"INSERT INTO {table} VALUES (%s, %s)", data)
    conn.commit()

    return json.dumps({
        'status': 'Ok',
    })
