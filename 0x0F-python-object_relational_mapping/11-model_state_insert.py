#!/usr/bin/python3
"""
This script adds the State object named 'Louisiana' to the
'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Establish a connection to the database and add a state
    named 'Louisiana' to the 'hbtn_0e_6_usa' database.
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

    # Create a new State object named 'Louisiana'
    lou_state = State(name='Louisiana')

    # Add the State object to the session and commit the changes
    session.add(lou_state)
    session.commit()

    # Print the id of the added State object
    print('{0}'.format(lou_state.id))

    # Close the session
    session.close()
