from peewee import *


class Timer(Model):
    title = CharField()
    started = DateTimeField(null=True)
    stopped = DateTimeField(null=True)
    total_time = DateTimeField(null=True)