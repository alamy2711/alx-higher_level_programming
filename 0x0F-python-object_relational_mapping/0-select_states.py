#!/usr/bin/python3
"""
This script retrieves and prints all states from the 'hbtn_0e_0_usa' database.
"""

import MySQLdb
from sys import argv


def retrieve_states_from_database(host, user, password, database_name):
    """
    Connect to the MySQL database and retrieve all states.

    Args:
        host (str): The database host.
        user (str): The database user.
        password (str): The database user's password.
        database_name (str): The name of the database.

    Returns:
        list: A list of tuples representing the retrieved states.
    """
    db = MySQLdb.connect(host=host, user=user, passwd=password,
                         db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    db.close()
    return rows


def print_states(states):
    """
    Print the retrieved states.

    Args:
        states (list): A list of tuples representing the states.
    """
    for state in states:
        print(state)


if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 5:
        print("Usage: {} <host> <user> <password> <database>".format(argv[0]))
        exit(1)

    host, user, password, database_name = argv[1:5]

    # Retrieve states from the database
    states = retrieve_states_from_database(host, user, password, database_name)

    # Print the retrieved states
    print_states(states)
