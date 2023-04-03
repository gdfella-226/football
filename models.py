from sqlalchemy import Column, Integer, Text, Date, Time, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Team(Base):
    __tablename__ = "teams"
    name = Column(Text)
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    coach = Column(Text)
    division = Column(Text)


class Tour(Base):
    __tablename__ = "tours"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(Text)
    date_start = Column(Date)
    date_end = Column(Date)
    field = Column(Text)


class Field(Base):
    __tablename__ = "fields"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(Text)
    ForeignKeyConstraint(["stadium"], ["Tour.field"])
    format = Column(Integer)
    start_time = Column(Time)
    duration = Column(Time)
    plays = Column(Integer)


class Games(Base):
    __tablename__ = "games"
    ss = Column(Integer, primary_key=True)
    ForeignKeyConstraint(["team1"], ["Team.id"])
    ForeignKeyConstraint(["team2"], ["Team.id"])
    flag = Column(Boolean)
    ForeignKeyConstraint(["tour"], ["Tour.id"])

