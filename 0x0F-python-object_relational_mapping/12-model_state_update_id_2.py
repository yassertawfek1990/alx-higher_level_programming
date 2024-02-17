#!/usr/bin/python3
""" prinsthts """
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
    nce = ss.query(State).filter_by(id=2).first()
    nce.name = 'New Mexico'
    ss.commit()
