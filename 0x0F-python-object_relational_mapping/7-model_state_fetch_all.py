#!/usr/bin/python3
""" a script that lists all State objects
from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
                            @localhost:3306/{argv[3]}')

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).order_by(State.id)

    states = query.all()

    for state in states:

        print(f'{state.id}: {state.name}')

    session.close()
