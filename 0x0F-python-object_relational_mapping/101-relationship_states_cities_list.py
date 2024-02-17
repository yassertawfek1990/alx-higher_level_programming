#!/usr/bin/python3
""" printbase """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    ge = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(ge)
    Sn = sessionmaker(bind=ge)
    ss = Sn()
    for i in ss.query(State).order_by(State.id):
        print(i.id, i.name, sep=": ")
        for c in i.cities:
            print("    ", end="")
            print(c.id, c.name, sep=": ")
