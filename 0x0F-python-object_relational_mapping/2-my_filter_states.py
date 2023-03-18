#!/usr/bin/python3

"""Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":

    import MySQLdb

    import sys

    connect = MySQLdb.connect(
                                host="localhost",
                                user=sys.argv[1],
                                password=sys.argv[2],
                                database=sys.argv[3]

                                )

    searched = sys.argv[4]
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id".format(searched))

    results = cursor.fetchall()

    for result in results:

        print(result)

    cursor.close()
    connect.close()
