#!/usr/bin/python3
"""
This script retrieves and prints all City objects from the 'hbtn_0e_14_usa'
database.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Establish a connection to the database and retrieve the cities
    from the 'hbtn_0e_14_usa' database.
    """

    # Create the database URI using the provided credentials
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create an SQLAlchemy engine and create tables if not exist
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)

    # Create a session class with the engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Create a new State object named 'California'
    cal_state = State(name='California')

    # Create a new City object named 'San Francisco'
    sfr_city = City(name='San Francisco')

    # Append the 'San Francisco' City to the 'California' State
    cal_state.cities.append(sfr_city)

    # Add the 'California' State to the session and commit the changes
    session.add(cal_state)
    session.commit()

    # Close the session
    session.close()
