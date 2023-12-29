#!/usr/bin/python3
"""Define the DBStorage engine"""
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from os import getenv


class DBStorage():
    """Manage the database for the HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        my_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            query = self.__session.query(cls)
            for value in query:
                key = "{}.{}".format(type(value).__name__, value.id)
                my_dict[key] = value
        else:
            class_list = [State, City, User, Place, Review, Amenity]
            for in_class in class_list:
                query = self.__session.query(in_class)
                for value in query:
                    key = "{}.{}".format(type(value).__name__, value.id)
                    my_dict[key] = value
        return (my_dict)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        item = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(item)
        self.__session = Session()

    def delete(self, obj=None):
        """ deletes an obj in the database """
        if obj:
            self.session.delete(obj)

    def close(self):
        """ closes the respective database """
        self.__session.close()
