from abc import ABC, abstractmethod
from typing import List
from models.comment import Comment

class ICommentsRepository(ABC):
    @abstractmethod
    def get_all_comments(self) -> List[Comment]:
        pass
