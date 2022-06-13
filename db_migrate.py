# project/db_migrate.py


from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime

print(DATABASE_PATH)

connection = sqlite3.connect(DATABASE_PATH)
cur = connection.cursor()

# temporarily  change the name of tasks table
#cur.execute('ALTER TABLE tasks RENAME TO old_tasks')

# create a new tasks table with the updated schema
#db.create_all()

# retrieve data from the old_tasks table
cur.execute('SELECT name, due_date, priority, status FROM old_tasks ORDER BY task_id ASC')

# save all rows as a list of tuples; set posted date to Now and users_id to 1
# use list comprehension
data = [
    (row[0], row[1], row[2], row[3], datetime.now(), 1) for row in cur.fetchall()
]

# insert data into the tasks table
cur.executemany('''INSERT INTO tasks (name, due_date, priority, status,
    posted_date, user_id) VALUES (?,?,?,?,?,?)''', data)

# commit changes
connection.commit()

# delet old_tasks table
#cur.execute('DROP TABLE old_tasks')