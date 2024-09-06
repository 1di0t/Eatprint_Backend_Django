from django.db import models

from geoalchemy2 import Geography



class Users(models.Model):
    user_num = models.IntegerField(primary_key=True, auto_increment=True)
    user_id = models.CharField(max_length=100, unique=True)
    user_pw = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)

class Users(db.Model):
    __tablename__ = 'user_tb'

    user_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(100), unique=True, nullable=False)
    user_pw = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    nick_name = db.Column(db.String(100), nullable=False)#True로 변경 고려

    posts = db.relationship('Post', back_populates='user',lazy = True)
class Post(db.Model):
    __tablename__ = 'post_tb'
    
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_num = db.Column(db.Integer, db.ForeignKey('user_tb.user_num'))
    content = db.Column(db.Text,nullable=True)
    location = db.Column(Geography(geometry_type='POINT', srid=4326),nullable=True)
    # created_date = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('Users', back_populates='posts')
    images = db.relationship('Image', back_populates='post',lazy = True)

class Image(db.Model):
    __tablename__ = 'image_tb'
    
    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post_tb.post_id'),nullable=False)
    url = db.Column(db.String(255), nullable=False)

    post = db.relationship('Post', back_populates='images')
    


class Hashtag(db.Model):
    __tablename__ = 'hashtag_tb'
    
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(50), nullable=False, unique=True)
    


posthashtag_table = db.Table('post_hashtag_tb',
    db.Column('post_id', db.ForeignKey('post_tb.post_id'), primary_key=True),
    db.Column('tag_id',  db.ForeignKey('hashtag_tb.tag_id'), primary_key=True)
)
