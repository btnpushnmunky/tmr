#!/usr/bin/env python
import argparse
from peewee import Model, CharField, DateTimeField, IntegerField, SqliteDatabase
from playhouse.csv_loader import dump_csv
from datetime import datetime
import os
import platform
from tabulate import tabulate


OS = platform.system()
user_dir = os.environ['HOME']

database = SqliteDatabase(os.path.join(user_dir, 'timers.db'))

table_header = ("ID", "Title")

def parse_time(time):
    hours = minutes = seconds = 0
    if time > 60:
        minutes, seconds = divmod(time, 60)
        if minutes > 60:
            hours, minutes = divmod(minutes, 60)
            if hours > 60:
                days, hours = divmod(hours, 24)

    return "Days: {0}, Hours: {1}, Minutes {2}, Seconds {3}".format(days, hours, minutes, seconds)

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
    print("Started: ")
    print(tabulate([[new_timer.id, new_timer.title]], table_header))


def stop(args):
    """
    Stop a timer with name.
    """
    timer = Timer.get(Timer.id == args.n)
    timer.stopped = datetime.now()
    timer.total_time = (timer.stopped - timer.started).total_seconds()
    timer.save()
    stopped_header = ["ID", "Title", "Total Time"]
    print("Stopped: ")
    time = parse_time(timer.total_time)
    data = [timer.id, timer.title, time]
    print(tabulate([data], stopped_header))


def list_timers(args):
    """
    List all running timers
    """
    timers = Timer.filter(Timer.stopped == None)  # noqa
    data = [[timer.id, timer.title] for timer in timers]
    print("\nRunning timers:")
    print(tabulate(data, table_header))


def export(args):
    if args.format == 'csv':
        with open(os.path.join(user_dir, 'timers.csv'), 'w') as f:
            timers = Timer.select()
            dump_csv(timers, f)
            print('Exported to timers.csv')
    elif args.format == 'html':
        print('Will export to html eventually')


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
    export_parser.add_argument('format', type=str, help='csv or html')
    export_parser.set_defaults(func=export)

    args = parser.parse_args()
    args.func(args)
