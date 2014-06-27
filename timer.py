from peewee import *
from datetime import datetime

class Timer(Model):
    title = CharField()
    started = DateTimeField()
    stopped = DateTimeField()
    total_time = DateTimeField()
