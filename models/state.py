#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """State class inherits from BaseModel and Base"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Retrieves a list of cities associated with the current instance.

            If the environment variable 'HBNB_TYPE_STORAGE' is not set to 'db',
            this method retrieves cities by iterating through all City
            instances stored in the models' storage and filtering them based
            on the matching state_id with the current instance.

            Returns:
                list: A list of City instances associated with
                      the current state.

            Note:
                This method assumes the existence of models.storage for data
                retrieval.
                If 'HBNB_TYPE_STORAGE' is set to 'db', it is expected to
                retrieve cities from a database.
            """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
