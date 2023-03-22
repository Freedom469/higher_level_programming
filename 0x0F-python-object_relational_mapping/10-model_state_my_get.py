#!/usr/bin/python3

""" a script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3])

                            )

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name == '{}'.format(argv[4]))\
                                .order_by(State.id)

    results = query.all()

    if not results:
        print("Not found")

    else:
        for result in results:

            print(f'{result.id}')

    session.close()
