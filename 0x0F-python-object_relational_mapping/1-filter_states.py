#!/usr/bin/python3

"""a script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connect = MySQLdb.connect(
                    host="localhost",
                    port=3306,
                    user=argv[1],
                    password=argv[2],
                    database=argv[3]

                    )

    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name \
                    LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)

    cursor.close()
    connect.close()
