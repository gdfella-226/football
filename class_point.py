import models


class Point:
    def __init__(self, team: models.Team):
        self.team = team
        self.potential = []
