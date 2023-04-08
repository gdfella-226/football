from class_day import Day
from itertools import groupby
import models
import create_fields
from class_point import Point
from database import init_db, SESSIONLOCAL, ENGINE


class Teams:
    def __init__(self, team):
        self.flag = None
        self.team = team


class Fields:
    def __init__(self, fieldd, dayy: Day):
        self.field = fieldd
        self.day = dayy


class Games:
    def __init__(self, team1, team2, time):
        self.team1 = team1
        self.team2 = team2
        self.time = time


init_db()
ENGINE.connect()
database = SESSIONLOCAL()

pr = database.query(models.Team).all()

mass_teams = []

for i in range(len(pr)):
    c = Teams(pr[i])
    mass_teams.append(c)
    if pr[i].time_wish is not None:
        mass_teams[i].flag = True

days_db = database.query(models.Field).all()

days = []

for i in range(len(days_db)):
    k = days_db[i]
    day = Day(days_db[i].start_time, days_db[i].duration)
    field = Fields(k, day)
    days.append(field)

mass_games = []

stadiums = []

for i in range(len(days_db)):
    stadiums.append(days_db[i].stadium)

stadiums = list(set(stadiums))


for i in range(len(stadiums)):
    f = stadiums[i]
    # массив в котором хранятся команда с пожеланием по определенному стадиону
    s = database.query(models.Team).filter(models.Team.stadium_wish == f).all()














