import datetime
from . import db

from marshmallow import Schema, fields

class Blog(db.Model):
    __tablename__ = "blog"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        now = datetime.datetime.now()
        self.date_created = now
        self.last_modified = now
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return f'Blog post successfully created.'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, old, data):
        for key, item in data.items():
            setattr(old, key, item)
        self.last_modified = datetime.datetime.utcnow()
        db.session.commit()
        return old

    @staticmethod
    def get_one_blog(post_id):
        return Blog.query.filter_by(id=post_id).first()

    @staticmethod
    def get_all_blogs():
        return Blog.query.all()

class BlogSchema(Schema):
    id = fields.Int(dump_only=False)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    user_id = fields.Str(required=True)
    date_created = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime(dump_only=True)