#!/usr/bin/python3
""" Contaibase() """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

ta = MetaData()
Base = declarative_base(metadata=ta)


class State(Base):
    """ Classate """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
