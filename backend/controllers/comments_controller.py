from flask import Blueprint, jsonify
import pymysql
from injector import inject
from flask.views import MethodView

from services.intertfaces.i_comments_service import ICommentsService

comments_bp = Blueprint('comments', __name__)

class CommentsController(MethodView):
    @inject
    def __init__(self, comments_service: ICommentsService):
        self.comments_service = comments_service

    def get(self):
        try:
            comments = self.comments_service.get_all_comments()
            return jsonify([comment.to_dict() for comment in comments])
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": str(e)}), 500

# クラスベースのビューをBlueprintに登録
comments_view = CommentsController.as_view('comments')
comments_bp.add_url_rule('/comments', view_func=comments_view)