from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    genre = db.Column(db.String(120))
    publish_date = db.Column(db.Date, index=True)
    read = db.Column(db.Boolean)
    rating = db.Column(db.Integer, index=True)
    complete_date = db.Column(db.Date, index=True)
    tags = db.Column(db.String(128))

    def __repr__(self):
        return f'<Book {self.title}>'
