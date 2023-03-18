#!/usr/bin/python3

""" a script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    try:
        connection = MySQLdb.connect(
                                        host="localhost",
                                        user=argv[1],
                                        password=argv[2],
                                        database=argv[3]

                                    )
        if connection:

            query = "SELECT * FROM cities ORDER BY id ASC"

            cursor = connection.cursor()

            cursor.execute(query)

            results = cursor.fetchall()

            if results:

                for result in results:

                    print(result)

            else:

                print("No match found")

    except MySQLdb.Error as e:

        print("Connection Failed", e)

    finally:
        cursor.close()
        connection.close()
