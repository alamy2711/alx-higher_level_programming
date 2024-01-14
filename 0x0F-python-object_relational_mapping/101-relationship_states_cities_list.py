#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects in the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Establishes a connection to the database and retrieves
    all State objects along with their corresponding City objects.
    """

    # Create the database URI using the provided credentials
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    # Create an SQLAlchemy engine and create tables if not exist
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session class with the engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query and retrieve all State objects with their
    # corresponding City objects
    states = session.query(State).outerjoin(City).order_by(State.id,
                                                           City.id).all()

    # Print the State and City information
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
