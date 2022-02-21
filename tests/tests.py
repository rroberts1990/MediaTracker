from datetime import datetime, timedelta
import pytest
from app import create_app, db
from app.models import User, Movie
from config_files.config import Config

class TestConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class TestUserModel:
    def __init__(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def test_password_hashing(self):
        u = User(username='Susan')
        u.set_password('cat')
        assert u.check_password('cat')

    def test_follow(self):
        u1 = User(username='Winston', email='winston@gmail.com')
        u2 = User(username='Joanna', email='joanna@gmail.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        assert u1.followed.all() == []
        assert u1.followers.all() == []

        u1.follow(u2)
        db.session.commit()

        assert u1.is_following(u2)
        assert u1.followed.count() == 1
        assert u1.followed.first().username == 'Joanna'
        assert u2.followers.count() == 1
        assert u2.followers.first().username == 'Winston'

        u1.unfollow(u2)
        db.session.commit()

        assert not u1.is_following(u2)

        assert u1.followed.count() == 0
        assert u2.followers.count() == 0


