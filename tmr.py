from timer import Timer
import click
from peewee import *
from datetime import datetime


@click.group()
def timer():
    pass


@timer.command(help='Create the database.')
def init():
    Timer.create_table(fail_silently=True)
    print("Created database.")


@timer.command(help='Create and start a timer.')
@click.option("--name", prompt="Name the timer")
def start(name):
    Timer.create_table(fail_silently=True)
    new_timer = Timer.create(title=name, started=datetime.now())
    new_timer.save()
    print("Created timer {0}".format(name))


@timer.command(help='Stop the timer.')
@click.option("--name", prompt="What's the name of the timer to stop?")
def stop(name):
    timer = Timer.get(Timer.title == name)
    timer.stopped = datetime.now()
    timer.total_time = (timer.stopped - timer.started).total_seconds()
    timer.save()
    print("Stopped {0}. You spent {1} seconds on this task.".format(
        timer.title, timer.total_time))


@timer.command(help='List running timers')
def list():
    print('List running timers.')


if __name__ == "__main__":
    timer()
