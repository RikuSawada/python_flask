from flask import Blueprint, jsonify
import pymysql

from db import conn

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/comments', methods=['GET'])
def get_comments():

    try:
        # データベース接続コード（例として、app.pyで作成したconnを使用）
        with conn.cursor() as cur:
            sql = "SELECT * FROM Comment"
            cur.execute(sql)
            results = cur.fetchall()
        return jsonify(results)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
