#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
 Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    sql_query = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(sql_query)

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()

    db.close()
