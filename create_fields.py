'''import models
from class_day import Day
from main import database

fields = [[]]
fields_mass = database.query(models.Field)
count_field = database.query(models.Field).count()

for i in range(count_field):
    start = database.query(models.Field.start_time).filter(models.Field.id == i)
    duration = database.query(models.Field.duration).filter(models.Field.id == i)
    c = Day(start, float(duration))
    k = [fields_mass.filter(models.Field.id == i), c]
    fields.append(k)
'''
