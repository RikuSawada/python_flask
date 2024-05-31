import os
import pymysql.cursors
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = pymysql.connect(
    host='db',
    port=3306,
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    db=os.environ.get('MYSQL_DATABASE'),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@app.route('/', methods=['GET'])
def select_all():
    with conn.cursor() as cur:
        sql = "SELECT * FROM Comment"
        cur.execute(sql)
        results = cur.fetchall()
    return jsonify(results)
