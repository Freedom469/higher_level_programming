#!/usr/bin/python3

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    try:
        connect = MySQLdb.connect(

                    host="localhost",
                    port=3306,
                    user=argv[1],
                    password=argv[2],
                    database=argv[3]

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
