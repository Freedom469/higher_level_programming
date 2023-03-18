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

    query = "SELECT cities.id,cities.name, states.name FROM cities \
    JOIN states ON \
    cities.state_id=states.id  ORDER BY cities.id ASC"

    cursor = connection.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    for result in results:

        print(result)

    cursor.close()
    connection.close()
