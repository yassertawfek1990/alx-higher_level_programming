#!/usr/bin/python3
""" prinasseda rn """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    ge = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(ge)
    Sn = sessionmaker(bind=ge)
    ss = Sn()
    for i in (ss.query(State.name, City.id, City.name)
              .filter(State.id == City.state_id)):
        print(i[0] + ": (" + str(i[1]) + ") " + i[2])
