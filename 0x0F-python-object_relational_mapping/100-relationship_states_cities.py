#!/usr/bin/python3
""" Createsthe CitDB """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    ge = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)
    Base.metadata.create_all(ge)
    Sn = sessionmaker(bind=ge)
    ss = Sn()
    ns = State(name='California')
    nc = City(name='San Francisco')
    ns.cities.append(newCity)
    ss.add(ns)
    ss.add(nc)
    ss.commit()
