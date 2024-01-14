#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the 'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Delete State objects from the database.
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

    # Delete all State objects with a name containing the letter 'a'
    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    # Commit the changes and close the session
    session.commit()
    session.close()
