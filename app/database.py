import hashlib

from datetime import datetime
from peewee import *

database = MySQLDatabase('fastapi_project', user='root',
                        password='', host='localhost', port=3306)


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)


    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'


    @classmethod
    def create_password(cls, password):
        hash = hashlib.md5()
        hash.update(password.encode('utf-8'))
        return hash.hexdigest()


class Movie(Model):
    title = CharField(max_length=50)
    year = IntegerField()
    director = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)


    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'


class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie)
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)


    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

    class Meta:
        database = database
        table_name = 'user_reviews'
