from peewee import *


class Timer(Model):
    title = CharField()
    started = DateTimeField(null=True)
    stopped = DateTimeField(null=True)
    # TODO: total_time needs to handle datetime.timedelta or convert to
    # datetime.time
    total_time = TimeField(null=True)