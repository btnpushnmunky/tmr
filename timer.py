from peewee import *

db = SqliteDatabase('timers.db')


class Timer(Model):
    title = CharField()
    started = DateTimeField()
    stopped = DateTimeField()
    total_time = DateTimeField()

    class Meta:
        database = db