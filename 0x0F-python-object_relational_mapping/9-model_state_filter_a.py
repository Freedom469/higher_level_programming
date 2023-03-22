#!/usr/bin/python3

""" a script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa"""

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3])
                            )

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))

    results = query.all()

    for result in results:

        print(f'{result.id}: {result.name}')

    session.close()
