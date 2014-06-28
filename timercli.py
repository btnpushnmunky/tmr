from timer import Timer
# import click


def create(name):
    new_timer = Timer(name=name)
    new_timer.save()
    pass


def start():
    pass


def stop():
    pass

if __name__ == "__main__":
    Timer.create_table(fail_silently=True)