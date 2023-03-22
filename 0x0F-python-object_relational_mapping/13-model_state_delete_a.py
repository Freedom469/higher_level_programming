#!/usr/bin/python3

""" a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3])
                            )

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))

    results = query.all()

    for result in results:

        session.delete(result)

    session.commit()

    session.close()
