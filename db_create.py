# project/db_create.py

from datetime import date

from project import db, bcrypt
from project.models import Task, User


# create the database and the db table
db.create_all()


# Insert dummy data into the table

db.session.add(
    User(name='admin', email='ad@min', password=bcrypt.generate_password_hash('admin'), role='admin')
)

db.session.add(
    Task(name='Finish this tutorial', due_date=date(2016, 9, 22), priority=8, status=1)
)

db.session.add(
    Task(name='Finish Real Python', due_date=date(2016, 10, 3), priority=10, status=1)
)


# commit the changes
db.session.commit()