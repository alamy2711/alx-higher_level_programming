#!/usr/bin/python3
"""
This script takes a command-line argument and displays all values
in the 'states' table where the 'name' column matches the provided
argument from the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish a connection to the database and retrieve the states
    while ensuring robust protection against MySQL injections.
    """

    # Connect to the database using the provided credentials
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Use a context manager for the cursor to ensure proper cleanup
    with db.cursor() as cursor:
        # Execute a parameterized query to select states with a specific name
        query = """
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """
        cursor.execute(query, {'name': argv[4]})

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

    # Display the retrieved states
    if rows is not None:
        for row in rows:
            print(row)
