from models import Run
from peewee import *

def search():
    for run in Run.select():
        print(run.date, run.fitness)


def addrun():
    # new_run = Run.()
    # new_run.save()
