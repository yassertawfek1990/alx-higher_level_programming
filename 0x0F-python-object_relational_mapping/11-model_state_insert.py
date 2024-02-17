#!/usr/bin/python3
""" printsthtatbcthe """
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
    nete = State(name='Louisiana')
    ss.add(nete)
    ne = ss.query(State).filter_by(name='Louisiana').first()
    print(ne.id)
    ss.commit()
