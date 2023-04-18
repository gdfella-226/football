from sqlalchemy import Column, Integer, Text, Date, Time, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Team(Base):
    __tablename__ = "teams"
    name = Column(Text)
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    coach = Column(Text)
    division = Column(Text)
    time_wish = Column(Text)
    stadium_wish = Column(Text)
    format = Column(Text)
    count_of_matches = Column(Integer, default=0)

class Tour(Base):
    __tablename__ = "tours"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(Text)
    date_start = Column(Text)
    date_end = Column(Text)
    ForeignKeyConstraint(["name"], ["Field.name"])

class Field(Base):
    __tablename__ = "fields"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(Text)
    stadium = Column(Text)
    format = Column(Integer)
    start_time = Column(Text)
    duration = Column(Text)
    games_amount = Column(Integer)


class Games(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    team1 = Column(Text)
    team2 = Column(Text)
    start_time = Column(Text)
    stadium = Column(Text)
    field = Column(Text)
    division = Column(Text)
