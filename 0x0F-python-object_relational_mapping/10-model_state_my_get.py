#!/usr/bin/python3
"""
This script retrieves and prints the State object id with the name passed
as an argument from the 'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Establish a connection to the database and retrieve a state
    with the specified name from the 'hbtn_0e_6_usa' database.
    """

    # Create the database URI using the provided credentials
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create an SQLAlchemy engine
    engine = create_engine(db_uri)

    # Create a session class with the engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query and retrieve the State object id with the specified name
    instance = session.query(State).filter(State.name == argv[4]).first()

    # Print 'Not found' if the instance is None, otherwise print the id
    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
