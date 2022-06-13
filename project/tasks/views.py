# project/tasks/views.py


# imports ###############################################################################

from datetime import datetime
from functools import wraps
from flask import flash, redirect, render_template, request, session, url_for, Blueprint

from .forms import AddTaskForm
from project import db
from project.models import Task



# config #################################################################################
tasks_blueprint = Blueprint('tasks', __name__)



# helper functions #######################################################################

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('Tou need to login first.')
            return redirect(url_for('login'))
    return wrapper

def open_tasks():
    open_tasks = db.session.query(Task) .filter_by(status='1').order_by(Task.due_date.asc())
    return open_tasks


def closed_tasks():    
    closed_tasks = db.session.query(Task).filter_by(status='0').order_by(Task.due_date.asc())
    return closed_tasks


# route handlers #############################################################################

# get all tasks
@tasks_blueprint.route('/tasks/')
@login_required
def tasks():
    return render_template(
        'tasks.html', 
        form = AddTaskForm(request.form),
        open_tasks = open_tasks(),
        closed_tasks = closed_tasks(),
        username = session['name']
    )


# Add new tasks
@tasks_blueprint.route('/add/', methods=['POST'])
@login_required
def new_task():
    error = None
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # Maak een nieuw object op basis van de properties
            new_task = Task(
                name = form.name.data,
                due_date = form.due_date.data,
                priority = form.priority.data,
                posted_date = datetime.utcnow(),
                status = 1,
                user_id = session['user_id']
             )
            # Voeg het object toe aan de sessie
            db.session.add(new_task)
            # Commit de wijziging
            db.session.commit()
            flash('New entry was successfully posted.')
            return redirect(url_for('tasks.tasks'))
        
    return render_template(
        'tasks.html',
        form=form,
        error=error,
        open_tasks=open_tasks(),
        closed_tasks=closed_tasks()
        )



# Mark tasks as complete
@tasks_blueprint.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    new_id = task_id
    # maak een object van het betreffende record
    rec = Task.query.filter_by(task_id=new_id).first()
    if session['user_id'] == rec.user_id or session['role'] == 'admin':
        # Pas de betreffende property aan
        rec.status = 0
        # Commit de wijziging
        db.session.commit()
        flash('The task was marked as complete.')
        return redirect(url_for('tasks.tasks'))
    else:
        flash('You can only update tasks that belong to you.')
        return redirect(url_for('tasks.tasks'))



# Delete tasks
@tasks_blueprint.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
    new_id = task_id
    # Maak een object van he betreffende record
    rec = Task.query.filter_by(task_id=new_id).first()
    if session['user_id'] == rec.user_id or session['role'] == 'admin':
        # Verwijder het corresponderende record in de sessie
        db.session.delete(rec)
        # Commit de wijziging
        db.session.commit()
        flash('The task was deleted.')
        return redirect(url_for('tasks.tasks'))
    else:
        flash('You can only delete tasks that belong to you.')
        return redirect(url_for('tasks.tasks'))

