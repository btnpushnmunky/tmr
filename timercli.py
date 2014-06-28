from timer import Timer
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()

def create(name):
    new_timer = Timer(name=name)
    new_timer.save()


def test():
    click.echo('test')


def start():
    pass


def stop():
    pass

if __name__ == "__main__":
    Timer.create_table(fail_silently=True)