import models
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
            models.Team.id == i) != database.query(models.Team.division).filter(models.Team.id == j):
            mass[i].potential.append(database.query(models.Team).filter(models.Team.id == j))
