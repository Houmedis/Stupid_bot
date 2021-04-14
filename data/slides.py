import sqlalchemy
from .db_session import SqlAlchemyBase


class Slides(SqlAlchemyBase):
    __tablename__ = 'slide'
    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    id_main = sqlalchemy.Column(sqlalchemy.Integer, default=True)
    games = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    movies = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    anime = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    music = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    li24 = sqlalchemy.Column(sqlalchemy.Boolean, default=True)