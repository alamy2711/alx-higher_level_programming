#!/usr/bin/python3
"""
This script takes the name of a state as a command-line argument and
lists all cities of that state using the database 'hbtn_0e_4_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish a connection to the database and retrieve the cities
    of the specified state from the database.
    """

    # Connect to the database using the provided credentials
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Use a context manager for the cursor to ensure proper cleanup
    with db.cursor() as cursor:
        # Execute the SQL query to select cities of the specified state
        query = """
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """
        cursor.execute(query, {'state_name': argv[4]})

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

    # Display the names of the retrieved cities
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
