How To
=======

Install
--------

Download the source, cd into the source folder, and run ``pip install .``. 

Commands
----------

tmr init
    This initializes the database. It only needs to be run once after installing tmr. It will create a database in             the user's home directory.

tmr start TITLE
    This will start a timer with the title TITLE.

tmr end ID
    Stop timer with the id ID.

tmr list
    List all running timers.

tmr export FORMAT
    Export all timers to a file as FORMAT. (Only CSV is currently working.)

