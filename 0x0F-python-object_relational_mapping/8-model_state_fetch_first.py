#!/usr/bin/python3
""" prin_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    ge = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                      .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(ge)
    Sn = sessionmaker(bind=ge)
    ss = Sn()
    i = ss.query(State).first()
    if i is None:
        print("Nothing")
    else:
        print(i.id, i.name, sep=": ")
