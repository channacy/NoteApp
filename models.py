from tabnanny import check
from app import db, login
from flask_login import UserMixin
from werkeug.security import generate_password_hash, check_password_hash, generate_password_hash
from datetime import datetime

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dymamic')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

class Post():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)