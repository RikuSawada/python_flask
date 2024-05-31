class Comment:
  def __init__(self, id, title, category, content):
    self.id = id
    self.title = title
    self.category = category
    self.content = content

  def to_dict(self):
    return {"id": self.id, "title": self.title, "category": self.category, "content": self.content}