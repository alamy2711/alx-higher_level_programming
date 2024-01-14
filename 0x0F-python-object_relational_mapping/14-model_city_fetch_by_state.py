#!/usr/bin/python3
"""
This script retrieves and prints all City objects from the 'hbtn_0e_14_usa'
database, including their associated State information.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Establish a connection to the database and retrieve the cities
    along with their associated states from the 'hbtn_0e_14_usa' database.
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

    # Define a query to retrieve City and State objects joined on the State
    query = session.query(City, State).join(State)

    # Print the retrieved City and State information
    for city, state in query.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    # Commit the changes and close the session
    session.commit()
    session.close()
