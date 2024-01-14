#!/usr/bin/python3
"""
This script retrieves and prints the first State object from the
'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Establish a connection to the database and retrieve a state
    from the 'hbtn_0e_6_usa' database.
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

    # Query and retrieve the first State object ordered by id
    instance = session.query(State).order_by(State.id).first()

    # Print the retrieved State object or 'Nothing' if it's None
    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
