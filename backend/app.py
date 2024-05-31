import os
import pymysql.cursors
from flask import Flask, request, jsonify
from flask_cors import CORS

from controllers.comments import comments_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(comments_bp)
