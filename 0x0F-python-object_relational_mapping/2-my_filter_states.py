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
    if connect:

        searched = sys.argv[4]
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM states WHERE BINARY name='{}'\
        ORDER BY id".format(searched))

        results = cursor.fetchall()

        if results:

            for result in results:

                print(result)

        else:

            print("No match found")

    else:

        print("Connection failed")

    cursor.close()
    connect.close()
