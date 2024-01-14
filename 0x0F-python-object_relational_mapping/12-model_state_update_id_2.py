#!/usr/bin/python3
"""
This script updates the name of a State object in the 'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Update the name of a State object in the database.
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

    # Query and retrieve the State object with id '2'
    ari_state = session.query(State).filter(State.id == '2').first()

    # Update the name of the State object to 'New Mexico'
    # and commit the changes
    ari_state.name = 'New Mexico'
    session.commit()

    # Close the session
    session.close()
