from typing import List
from repositories.interfaces.i_comments_repository import ICommentsRepository
from models.comment import Comment
from services.intertfaces.i_comments_service import ICommentsService
from injector import inject

class CommentsService(ICommentsService):
    @inject
    def __init__(self, comments_repository: ICommentsRepository):
        self.comments_repository = comments_repository

    def get_all_comments(self) -> List[Comment]:
        return self.comments_repository.get_all_comments()
