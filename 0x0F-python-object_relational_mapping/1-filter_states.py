#!/usr/bin/python3
"""Lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve states starting with 'N' sorted by id
    c.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")
    [print(state) for state in c.fetchall()]

