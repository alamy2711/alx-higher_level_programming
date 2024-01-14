#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and retrieve the states.
    """
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Extracting command-line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=username, port=3306,
                         passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Display the retrieved states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
