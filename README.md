# Tmr - Simple job tracking timer to run from your terminal. 

Tmr uses Python and an SQlite database to store your timed events. Tmr's only dependency outside of Python's stdlib is [Peewee](https://github.com/coleifer/peewee), an easy to use ORM. Written with Python 3.4 in mind, but it *should* work in most version 2.7+.

## To install:

Download the source, cd into the source folder, and run `pip install .`. Eventually I hope to get it up on PyPI.

## Example usage after installation:

###### `tmr init`

This will initialize your database. It only needs to be run once after installation.

###### `tmr start TITLE`

This will start a timer with the title TITLE.

###### `tmr end TITLE`

This will end a timer with the title TITLE.

###### `tmr list`

This will list all running timers.

###### `tmr export`

This will export the timers to a csv file.
