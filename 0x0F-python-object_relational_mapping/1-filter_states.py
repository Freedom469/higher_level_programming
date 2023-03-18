#!/usr/bin/python3

"""a script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa:"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    connect = MySQLdb.connect(
                host="localhost",
                user=argv[1],
                password=argv[2],
                database=argv[3]

                )

    if (connect):

        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM states WHERE name
                        LIKE "N%" ORDER BY id""")

        results = cursor.fetchall()

        if results:

            for result in results:

                print(result)

        else:

            print("No match Found")
    else:
        print("Connection failed")

    cursor.close()
    connect.close()
