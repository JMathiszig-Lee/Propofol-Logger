from peewee import *

db = SqliteDatabase('runs.db')

class BaseModel(Model):
    class Meta:
        database = db

class Run(BaseModel):
    date = DateTimeField()
    modelName = TextField()
    fitness = DecimalField()
