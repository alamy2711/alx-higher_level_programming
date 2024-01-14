#!/usr/bin/python3
"""
This script defines a State class and a Base class for interacting
with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name associated with the class
        id (int): The unique identifier for a State instance
        name (str): The name of the State instance
        cities (:obj:`City`): The Cities associated with the State

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
