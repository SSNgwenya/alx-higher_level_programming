#!/usr/bin/python3
"""
This module lists all states from the MySQL database.
"""

import sys
import MySQLdb

def list_states(username, password, database):
    """
    Lists all states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute SQL query to fetch all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the query result
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)

        # Close the database connection
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 your_script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)

