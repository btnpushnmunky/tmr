from timer import Timer
import click
from peewee import *

# parser = argparse.ArgumentParser()
# parser.add_argument('--create_db', help='Create the database', action='store_true')
# args = parser.parse_args()
#
# if args.create_db:
#    print("Creating database...")
#    Timer.create_table(fail_silently=True)
#    print("Created timers.db.")
DB_NAME = 'timers.db'

@click.group()
def timer():
    database = SqliteDatabase(DB_NAME)
    database.connect()


@timer.command(help='Create the database.')
def init(name):
    Timer.create_table(fail_silently=True)


@timer.command(help='Create and start a timer.')
@click.option("--name", prompt="Name the timer")
def start(name):
    new_timer = Timer(name=name)
    new_timer.save()
    # Mark timer as running. Probably need to provide a timer name
    print('starting')


@timer.command(help='Stop the timer.')
def stop():
    print('stopping')

@timer.command(help='List running timers')
def list():
    print('List running timers.')
if __name__ == "__main__":
    timer()
