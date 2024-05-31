from db import conn
from models.comment import Comment

class CommentsRepository:
  @staticmethod
  def get_all_comments():
    with conn.cursor() as cur:
      sql = "SELECT * FROM Comment"
      cur.execute(sql)
      results = cur.fetchall()
      return [Comment(**row) for row in results]
