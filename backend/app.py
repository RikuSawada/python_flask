import os
import pymysql.cursors
from flask import Flask, request, jsonify
from flask_cors import CORS
from injector import Binder, singleton
from flask_injector import FlaskInjector

from controllers.comments_controller import comments_bp

from controllers.comments_controller import comments_bp, CommentsController
from services.comments_service import CommentsService
from services.intertfaces.i_comments_service import ICommentsService
from repositories.comments_repository import CommentsRepository
from repositories.interfaces.i_comments_repository import ICommentsRepository

app = Flask(__name__)

def configure(binder: Binder) -> Binder:
    binder.bind(ICommentsRepository, to=CommentsRepository, scope=singleton)
    binder.bind(ICommentsService, to=CommentsService, scope=singleton)
    binder.bind(CommentsController, to=CommentsController, scope=singleton)
    return binder

CORS(app)

app.register_blueprint(comments_bp)

FlaskInjector(app=app, modules=[configure])
