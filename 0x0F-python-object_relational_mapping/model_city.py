#!/usr/bin/python3
"""
This script defines a City class for use with MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name associated with the class
        id (int): The unique identifier for a City instance
        name (str): The name of the City instance
        state_id (int): The foreign key referencing the associated State

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
