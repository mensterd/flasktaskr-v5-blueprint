# project/models.py

# Docs: https://flask-sqlalchemy.palletsprojects.com/en/2.x/


from project import db
import datetime


class Task(db.Model):

    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return f'<name {self.name}>'


class User(db.Model):

        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique=True, nullable=False)
        email = db.Column(db.String, unique=True, nullable=False)
        password = db.Column(db.String, nullable=False)
        tasks = db.relationship('Task', backref='poster')
        role = db.Column(db.String, default='user')


        def __repr__(self):
            return f'User {self.name}'
