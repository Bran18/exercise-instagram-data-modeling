import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()




class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    user_from_id = Column(Integer, ForeignKey('follower.user_from_id'))
    

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, nullable=False)
    user = relationship(User)
    id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    coomentText = Column(String(250), nullable=False)
    authpr_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)

    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    typePost = Column(String(250), nullable=False)
    URLPost = Column(String(250), nullable=False)
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e