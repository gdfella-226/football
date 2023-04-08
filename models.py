from sqlalchemy import Column, Integer, Text, Date, Time, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(Text)
    division = Column(Text)
    format = Column(Integer) #
    coach = Column(Text)
    date = Column(Text) #
    stadium_wish = Column(Text)
    time_wish = Column(Text)
    time_wish2 = Column(Text) #
    #match_time = Column(Text)

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
    format = Column(Integer)
    date = Column(Text)
    stadium = Column(Text)
    name = Column(Text)
    start_time = Column(Text)
    duration = Column(Text)
    plays_amount = Column(Integer)


class Games(Base):
    __tablename__ = "games"
    ss = Column(Integer, primary_key=True)
    ForeignKeyConstraint(["team1"], ["Team.id"])
    ForeignKeyConstraint(["team2"], ["Team.id"])
    flag = Column(Boolean)
    ForeignKeyConstraint(["tour"], ["Tour.id"])

