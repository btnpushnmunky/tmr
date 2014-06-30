from peewee import *


class Timer(Model):
    title = CharField()
    started = DateTimeField()
    stopped = DateTimeField()
    total_time = DateTimeField()