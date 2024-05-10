#!/usr/bin/python3
"""Module that lists all cities from the hbtn_0e_4_usa database for a given state."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    # and Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve cities in the specified state
    query = ("SELECT DISTINCT c.name FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                WHERE `s`.`name` = %s \
                ORDER BY c.name")  # Updated ORDER BY clause
    c.execute(query, (sys.argv[4],))

    # Fetch all rows and print the cities separated by commas
    cities = [city[0] for city in c.fetchall()]
    print(", ".join(cities))

