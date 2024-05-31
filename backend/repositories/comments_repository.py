from typing import List
from db import conn
from models.comment import Comment
from repositories.interfaces.i_comments_repository import ICommentsRepository

class CommentsRepository(ICommentsRepository):
    def get_all_comments(self) -> List[Comment]:
        with conn.cursor() as cur:
            sql = "SELECT * FROM Comment"
            cur.execute(sql)
            results = cur.fetchall()
            return [Comment(**row) for row in results]
