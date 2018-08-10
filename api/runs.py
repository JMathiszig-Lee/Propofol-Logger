from models import Run
from peewee import *
from flask import request


response = "hello"

def search():
    get_response = []
    for run in Run.select():
        print(run.date, run.fitness)
        response_obj = {
            "date" : run.date,
            "fitness" : run.fitness,
            "model" : run.modelName
        }
        get_response.append(response_obj)
    return get_response


def post():

    print(request.json['fitness'])
    new_fit = request.json['fitness']
    new_date = request.json['date']
    new_model= request.json['model']

    new_run = Run(date = new_date, modelName = new_model, fitness = new_fit)
    new_run.save()

    return response
