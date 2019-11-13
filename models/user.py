import datetime
from . import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50))
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, email, password, first_name, last_name=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        now = datetime.datetime.now()
        self.date_created = now
        self.last_modified = now
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return f'User successfully created.'
