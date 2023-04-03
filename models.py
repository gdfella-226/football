from ctypes import Union
from enum import Enum

from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Text, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    name = Column(Text)
    id = Column(Integer, primary_key=True)
    coach = Column(Text)
    division = Column(Text)

class Tour(Base):
    __tablename__ = "tours"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_start = Column(Date)
    date_end = Column(Date)
    field = Column(Text)

class Field(Base):
    __tablename__ = "fields"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    stadium = Column(Tour.field)
    format = Column(Integer)
    start_time = Column(Time)
    duration = Column(Time)
    plays = Column(Integer)

