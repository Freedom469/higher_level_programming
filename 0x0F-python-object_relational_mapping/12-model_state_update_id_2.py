#!/usr/bin/python3

"""a script that changes the name of a State object from the database
hbtn_0e_6_usa"""

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

    state = session.query(State).filter_by(id=2).first()

    state.name = 'New Mexico'

    session.commit()

    session.close()
