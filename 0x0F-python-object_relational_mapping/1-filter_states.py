#!/usr/bin/python3

"""a script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa:"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    try:
        connect = MySQLdb.connect(
                    host="localhost",
                    user=argv[1],
                    password=argv[2],
                    database=argv[3]

                    )

    except MySQLdb.Error:
        print("Connection failed")

    cursor = connect.cursor()

    try:

        cursor.execute("""SELECT * FROM states WHERE name
                        LIKE "N%" ORDER BY id ASC""")

        results = cursor.fetchall()

        if results:

            for result in results:

                print(result)

        else:

            print("No match Found")

    except MySQLdb.Error:
        print("Connection failed")

    finally:
        cursor.close()
        connect.close()
