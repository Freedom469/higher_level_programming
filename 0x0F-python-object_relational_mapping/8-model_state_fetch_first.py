#!/usr/bin/python3

""" a script that prints the first State object from the database
hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

username = argv[1]
password = argv[2]
database = argv[3]

engine = create_engine(f"mysql://{username}:{password}"
                       f"@localhost:3306/{database}")


Session = sessionmaker(bind=engine)

session = Session()

query = session.query(State).order_by(State.id)

first = query.first()

if not first:
    print("Nothing")

else:

    print(f'{first.id}: {first.name}')
