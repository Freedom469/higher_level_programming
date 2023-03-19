#!/usr/bin/python3

""" a script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
                                        host="localhost",
                                        user=argv[1],
                                        password=argv[2],
                                        database=argv[3]

                                )

    query = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE BINARY  states.name = '{}'\
            ORDER BY cities.id".format(argv[4])

    cursor = connection.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    print(", ".join(result[0] for result in results))

    cursor.close()
    connection.close()
