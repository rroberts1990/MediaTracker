from datetime import datetime, timedelta
import pytest
from app import create_app, db
from app.models import User, Movie
from config_files.config import Config

class TestConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase:

    def test_password_hashing(self):
        u = User(username='Susan')
        u.set_password('cat')
        assert u.check_password('cat')
