from timer import Timer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--create_db', help='Create the database', action='store_true')
args = parser.parse_args()

if args.create_db:
    Timer.create_table(fail_silently=True)

def create(name):
    new_timer = Timer(name=name)
    new_timer.save()


def test():
    click.echo('test')


def start():
    pass


def stop():
    pass

    