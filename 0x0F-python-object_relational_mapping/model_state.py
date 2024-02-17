#!/usr/bin/python3
"""
Contaideclarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

ta = MetaData()
Base = declarative_base(metadata=ta)


class State(Base):
    """
    lste
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
