#!/usr/bin/python3

"""This Module lists all states from mySQL database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """lists all states from the database hbtn_0e_0_usa.
    Ags:
        username: mysql username
        password: mysql password
        database: mysql database
    """
    # Connects to MySQL server
    db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    cursor = db.cursor()

    # Execute SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches all rows from the query result
    rows = cursor.fetchall()

    # Prints results
    for row in rows:
        print(row)

    # Closes the database connection
    db.close()

    # Example usage
if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
