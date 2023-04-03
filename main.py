from sqlalchemy.orm import Session

import models
from database import init_db, SESSIONLOCAL, ENGINE

init_db()
ENGINE.connect()
database = SESSIONLOCAL()

class Point:
    def __init__(self, team):
        self.team = models.Team
        self.potential = []


row = models.Team(name="asd", coach="dasads", division="sadasd")

database.add(row)
database.commit()

rows = database.query(models.Team).count()

print(rows)
