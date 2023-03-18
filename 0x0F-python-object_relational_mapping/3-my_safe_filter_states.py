#!/usr/bin/python3

""" a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections!"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
                                    host="localhost",
                                    user=argv[1],
                                    password=argv[2],
                                    database=argv[3]

                                    )

    cursor = connection.cursor()
    searched = argv[4]

    query = "SELECT * FROM states WHERE BINARY name=%s ORDER BY id ASC"

    cursor.execute(query, (searched,))

    results = cursor.fetchall()

    for result in results:

        print(result)

    cursor.close()
    connection.close()
