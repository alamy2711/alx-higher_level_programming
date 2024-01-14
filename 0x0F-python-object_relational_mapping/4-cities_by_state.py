#!/usr/bin/python3
"""
This script lists all cities from the 'cities' table in the database
'hbtn_0e_4_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish a connection to the database and retrieve the cities
    along with their corresponding states from the database.
    """

    # Connect to the database using the provided credentials
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Use a context manager for the cursor to ensure proper cleanup
    with db.cursor() as cursor:
        # Execute the SQL query to select cities
        # with their corresponding states
        query = """
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """
        cursor.execute(query)

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

    # Display the retrieved cities and their corresponding states
    if rows is not None:
        for row in rows:
            print(row)
