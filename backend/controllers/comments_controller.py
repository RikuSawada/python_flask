from flask import Blueprint, jsonify
import pymysql

from db import conn

from services.comments_service import CommentsService

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/comments', methods=['GET'])
def get_comments():
    try:
        comments = CommentsService.get_all_comments()
        return jsonify([comment.to_dict() for comment in comments])
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
