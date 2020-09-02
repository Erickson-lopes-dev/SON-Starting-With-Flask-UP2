from app2.config import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(90))
    body = db.Column('body', db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f'Posts {self.title}'
