from timer import Timer
import argparse
import click

#parser = argparse.ArgumentParser()
#parser.add_argument('--create_db', help='Create the database', action='store_true')
#args = parser.parse_args()
#
#if args.create_db:
#    print("Creating database...")
#    Timer.create_table(fail_silently=True)
#    print("Created timers.db.")

def create(name):
    new_timer = Timer(name=name)
    new_timer.save()

@click.group()
def test():
    click.echo('test')

@test.command()
def start():
    pass

@test.command()
def stop():
    pass

    
