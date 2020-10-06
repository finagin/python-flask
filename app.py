#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json
import os
import psycopg2
import sqlite3
from flask import Flask, escape, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

table = 'requests'

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')


@app.route('/', methods=['GET', 'POST'])
def hello():
    cursor = conn.cursor()

    data = [
        (
            request.data.decode('utf-8'),
            json.dumps({
                'args': request.args if request.args else None,
                'form': request.form if request.form else None,
                'files': request.files if request.files else None,
                'json': request.json if request.json else None,
                'values': request.values if request.values else None,
            }),
        ),
    ]

    cursor.executemany(f"INSERT INTO {table} VALUES (%s, %s)", data)
    conn.commit()

    return json.dumps({
        'status': 'Ok',
    })
