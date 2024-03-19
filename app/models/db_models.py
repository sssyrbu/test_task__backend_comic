from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..database import Base


class Comic(Base):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    rating = Column(Float)


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, unique=True)
    comic_id = Column(Integer, ForeignKey("comics.id"))
    user_id = Column(Integer)
    value = Column(Float)