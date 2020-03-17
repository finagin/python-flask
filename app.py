import json
import logging
import sqlite3
from flask import Flask, escape, request, send_file

app = Flask(__name__)

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(filename='logs.log', format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.info('%s', 'Start App', extra=d)

table = 'requests'

conn = sqlite3.connect("db.sqlite3")
try:
    cursor = conn.cursor()
    cursor.execute(f"""CREATE TABLE {table}
                       (data text, args text)
                   """)
    conn.commit()
except sqlite3.OperationalError:
    logger.warning('table "%s" already exists', table, extra=d)
finally:
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def hello():
    conn = sqlite3.connect("mydatabase.sqlite")
    cursor = conn.cursor()

    try:
        try:
            data = [
                (
                    request.data,
                    json.dumps(request.args),
                ),
            ]
        except:
            logger.warning('Can\'t json dump', extra=d)

        cursor.executemany(f"INSERT INTO {table} VALUES (?, ?)", data)
        conn.commit()
    except:
        logger.warning('Can\'t insert into "%s"', table, extra=d)

    return json.dumps({
        'status': 'Ok',
    })


@app.route('/download')
def download_file():
    path = "./db.sqlite3"
    return send_file(path, as_attachment=True)


@app.route('/data')
def data():
    conn = sqlite3.connect("mydatabase.sqlite")
    cursor = conn.cursor()
    cursor.execute(f"select * from {table}")
    data = cursor.fetchall()

    return json.dumps(data)
