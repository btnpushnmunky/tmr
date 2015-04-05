#!/usr/bin/env python
import argparse
# import click
from peewee import *
from datetime import datetime


database = SqliteDatabase('timers.db')


class Timer(Model):
    title = CharField()
    started = DateTimeField(null=True)
    stopped = DateTimeField(null=True)
    total_time = IntegerField(null=True)

    class Meta:
        database = database


def main():
    parser = argparse.ArgumentParser(description='Time events')
    parser.add_argument('-i', '--init', help='Initialize the timer database',
                        action='store_true')
    parser.add_argument('-s', '--start', help='Start a timer')
    parser.add_argument('-e', '--end', help='End a timer')
    parser.add_argument('-l', '--list', help='List running timers', action="store_true")
    args = parser.parse_args()

    if args.init:
        init()
    elif args.start:
        start(args.start)
    elif args.end:
        stop(args.end)
    elif args.list:
        list_timers()


def init():
    Timer.create_table(fail_silently=True)
    print("Created database.")


def start(name):
    Timer.create_table(fail_silently=True)
    new_timer = Timer.create(title=name, started=datetime.now())
    new_timer.save()
    print("Created timer {0}".format(name))


def stop(name):
    timer = Timer.get(Timer.title == name)
    timer.stopped = datetime.now()
    timer.total_time = (timer.stopped - timer.started).total_seconds()
    timer.save()
    print("Stopped {0}. You spent {1} seconds on this task.".format(
        timer.title, timer.total_time))


def list_timers():
    timers = Timer.filter(Timer.stopped==None)
    for timer in timers:
        print("{0} has not been stopped.".format(timer.title))
