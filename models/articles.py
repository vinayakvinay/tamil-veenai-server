from sqlalchemy import Column, String, Integer, Date
from base import Base

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    tag = Column(String)
    category = Column(String)
    claps = Column(Integer)
    created_at = Column(Date)
    updated_at = Column(Date)

    def __init__(self, title, description, tag, category, claps, created_at, updated_at):
        self.title = title
        self.description = description
        self.tag = tag
        self.category = category
        self.claps = claps
        self.created_at = created_at
        self.updated_at = updated_at
