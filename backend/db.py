import os
import time
import pymysql.cursors

# データベース接続の初期化
conn = None
while True:
    try:
        conn = pymysql.connect(
            host='db',
            port=3306,
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            db=os.environ.get('MYSQL_DATABASE'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        break
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        time.sleep(5)