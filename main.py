import models
import create_fields
from class_point import Point
from database import init_db, SESSIONLOCAL, ENGINE


init_db()
ENGINE.connect()
database = SESSIONLOCAL()

mass = []

# row = models.Team(name="asd", coach="dasads", division="sadasd", )

# database.add(row)
# database.commit()

rows = database.query(models.Team).count()
teams = database.query(models.Team)
divisions = database.query(models.Team.division)
format = database.query(models.Team.format)

for i in range(rows):
    team = teams.filter(
        models.Team.id == i)
    c = Point(team)
    mass.append(c)

for i in range(rows):
    mass_time = []
    thin = database.query(models.Team.time_wish)
    mass_time.append(thin.filter(models.Team.id == i).first())
    mass_time.append(thin.filter(models.Team.id == i).last())
    for j in range(rows):
        mass_union_time = []
        mass_union_time.append(thin.filter(models.Team.id == j).first())
        mass_union_time.append(thin.filter(models.Team.id == j).last())
        coachthin = database.query(models.Team.stadium_wish)
        if (mass_time[1] <= mass_union_time[0] or mass_time[0] <= mass_union_time[0] or mass_time[0] <= mass_union_time[
            0] or
            mass_time[0] <= mass_union_time[1] or len(mass_time) == 0 or len(mass_union_time) == 0) and mass[
            i].team.coach != mass[j].team.coach and \
                coachthin.filter(models.Team.id[i]) == coachthin.filter(models.Team.id[j]) or \
                coachthin.filter(models.Team.id[i]) == "" or coachthin.filter(
            models.Team.id[j]) == "" and database.query(models.Team.division).filter(
            models.Team.id == i) != database.query(models.Team.division).filter(models.Team.id == j) and \
                divisions.filter(models.Team.id == i) == divisions.filter(models.Team.id == j) and \
                format.filter(models.Team.id == i) == format.filter(models.Team.id == j):
            mass[i].potential.append([models.Team(database.query(models.Team).filter(models.Team.id == j))])


for i in range(len(mass)):
    mass_time_for_point = str(mass[i].team.time_wish).split("-")
    left_limit_mass = mass_time_for_point[0].split(":")
    left_limit = int(left_limit_mass[0]) + round(1/int(left_limit_mass[1]), 2)
    right_limit_mass = mass_time_for_point[1].split(":")
    right_limit = int(right_limit_mass[0]) + round(1/int(right_limit_mass[1]), 2)
    for j in range(len(mass[i].potential)):
        mass_time_for_potential = str(models.Team(mass[i].potential[j]).time_wish).split("-")
        left_limit_mass_potential = mass_time_for_potential[0].split(":")
        left_limit_potential = int(left_limit_mass_potential[0]) + round(1/int(left_limit_mass_potential[1]), 2)
        right_limit_mass_potential = mass_time_for_potential[1].split(":")
        right_limit_potential = int(right_limit_mass_potential[0]) + round(1 / int(right_limit_mass_potential[1]), 2)

for i in range(len(mass)):
    for j in range(len(mass[i].potential)):
        pass







