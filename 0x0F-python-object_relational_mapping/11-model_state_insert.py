#!/usr/bin/python3

"""a script that adds the State object “Louisiana” to the database
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

    new_state = State(name='Louisiana')

    session.add(new_state)

    session.commit()

    print(f'{new_state.id}')

    session.close()
