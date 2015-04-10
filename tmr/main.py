#!/usr/bin/env python
import argparse
from peewee import *
from datetime import datetime
import os
import platform
import csv

OS = platform.system()
user_dir = os.environ['HOME']

database = SqliteDatabase(os.path.join(user_dir, 'timers.db'))


class Timer(Model):
    title = CharField()
    started = DateTimeField(null=True)
    stopped = DateTimeField(null=True)
    total_time = IntegerField(null=True)

    class Meta:
        database = database


def init():
    """
    Initialize the database.
    """
    Timer.create_table(fail_silently=True)
    print("Created database.")


def start(name):
    """
    Start a timer with name.
    """
    Timer.create_table(fail_silently=True)
    new_timer = Timer.create(title=name, started=datetime.now())
    new_timer.save()
    print("Created timer {0}".format(name))


def stop(name):
    """
    Stop a timer with name.
    """
    timer = Timer.get(Timer.title == name)
    timer.stopped = datetime.now()
    timer.total_time = (timer.stopped - timer.started).total_seconds()
    timer.save()
    print("Stopped {0}. You spent {1} seconds on this task.".format(
        timer.title, timer.total_time))


def list_timers():
    """
    List all running timers
    """
    timers = Timer.filter(Timer.stopped == None)
    for timer in timers:
        print("{0} has not been stopped.".format(timer.title))


def export(dest):
    pass


def main():
    parser = argparse.ArgumentParser(description='Time events')
    subcommands = parser.add_subparsers(help="Additional commands")
    init_parser = subcommands.add_parser('init', help="Initialize the timer database") 
    init_parser.set_defaults(func=init)
    parser.add_argument('-s', '--start', help='Start a timer')
    parser.add_argument('-e', '--end', help='End a timer')
    parser.add_argument('-l', '--list', help='List running timers',
                        action="store_true")
    parser.add_argument('-ex', '--export', help='Export your timers')
    args = parser.parse_args()
    args.func()
    #if args.init:
    #    init()
    #elif args.start:
    #    start(args.start)
    #elif args.end:
    #    stop(args.end)
    #elif args.list:
    #    list_timers()

