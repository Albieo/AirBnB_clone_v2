#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User class inherits from BaseModel and Base"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", cascade="all, delete, delete-orphan",
                          backref="user")
    reviews = relationship("Review", cascade="all, delete, delete-orphan",
                           backref="user")
