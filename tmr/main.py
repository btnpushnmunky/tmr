#!/usr/bin/env python
import argparse
from peewee import *
from playhouse.csv_loader import dump_csv
from datetime import datetime
import os
import platform


OS = platform.system()
user_dir = os.environ['HOME']

database = SqliteDatabase(os.path.join(user_dir, 'timers.db'))

table_header = "\nId\t| Title\n-------------"


class Timer(Model):
    title = CharField()
    started = DateTimeField(null=True)
    stopped = DateTimeField(null=True)
    total_time = IntegerField(null=True)

    class Meta:
        database = database


def init(args):
    """
    Initialize the database.
    """
    Timer.create_table(fail_silently=True)
    print("Created database.")


def start(args):
    """
    Start a timer with name.
    """
    Timer.create_table(fail_silently=True)
    new_timer = Timer.create(title=args.n, started=datetime.now())
    new_timer.save()
    print("\nStarted: \n{0}".format(table_header))
    print("{0}\t| {1}".format(new_timer.id, new_timer.title))
    print("\n")


def stop(args):
    """
    Stop a timer with name.
    """
    timer = Timer.get(Timer.id == args.n)
    timer.stopped = datetime.now()
    timer.total_time = (timer.stopped - timer.started).total_seconds()
    timer.save()
    print("\nStopped:\n{0}".format(table_header))
    print("{0}\t| {1} \nYou spent {2} seconds on this task.".format(
        timer.id, timer.title, timer.total_time))
    print("\n")


def list_timers(args):
    """
    List all running timers
    """
    timers = Timer.filter(Timer.stopped == None)  # noqa
    print("\nRunning timers:")
    print("\nId | Title\n-------------")
    for timer in timers:
        print("{0}  | {1}".format(timer.id, timer.title))
    print("\n")


def export(args):
    with open(os.path.join(user_dir, 'timers.csv'), 'w') as f:
        timers = Timer.select()
        dump_csv(timers, f)


def main():
    parser = argparse.ArgumentParser(description='Time events')
    subcommands = parser.add_subparsers(help="Additional commands")
    # Init parser
    init_parser = subcommands.add_parser('init',
                                         help="Initialize the timer database")
    init_parser.set_defaults(func=init)
    # New timer parser
    new_item_parser = subcommands.add_parser('start', help='Start a timer')
    new_item_parser.add_argument('n', type=str)
    new_item_parser.set_defaults(func=start)
    # List timers parser
    list_timers_parser = subcommands.add_parser('list',
                                                help='List running timers')
    list_timers_parser.set_defaults(func=list_timers)
    # Stop timer parser
    stop_timer_parser = subcommands.add_parser('stop', help='Stop a timer')
    stop_timer_parser.add_argument('n', type=str)
    stop_timer_parser.set_defaults(func=stop)
    # Export timers parser
    export_parser = subcommands.add_parser('export', help='Export the timers')
    export_parser.set_defaults(func=export)

    args = parser.parse_args()
    args.func(args)
