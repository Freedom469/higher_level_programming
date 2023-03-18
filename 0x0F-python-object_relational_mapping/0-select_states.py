#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    try:
        connect = MySQLdb.connect(

                    host="localhost",
                    port=3306,
                    user=sys.argv[1],
                    password=sys.argv[2],
                    database=sys.argv[3]

                    )

        cursor = connect.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id")

        results = cursor.fetchall()

        for result in results:

            print(result)

    except MySQLdb.Error:

        print('Operation Failed')

    finally:

        cursor.close()
        connect.close()
