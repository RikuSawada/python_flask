from repositories.comments_repository import CommentsRepository

class CommentsService:
  @staticmethod
  def get_all_comments():
    return CommentsRepository.get_all_comments()