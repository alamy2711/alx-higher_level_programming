#!/usr/bin/python3
"""
This script retrieves and displays all values in the 'states' table
where the 'name' column matches the provided argument
from the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish a connection to the database and retrieve the states
    where the 'name' column matches the provided argument.
    """

    # Connect to the database using the provided credentials
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select states with a specific name
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC".format(argv[4])
    cursor.execute(query)

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Display the retrieved states
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
