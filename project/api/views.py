# project/api/views.py

# docs ########################################################################
# https://flask-restful.readthedocs.io/en/latest/
# https://flask.palletsprojects.com/en/2.1.x/api/#flask.json.jsonify
# https://flask.palletsprojects.com/en/2.1.x/api/#flask.make_response

# imports #####################################################################

from flask import Blueprint, jsonify, make_response

from project import db
from project.models import Task



# config ######################################################################
api_blueprint = Blueprint('api', __name__)



# routes ######################################################################

@api_blueprint.route('/api/v1/tasks/<int:task_id>')
def task(task_id):
    #result = db.session.query(Task).filter_by(task_id=task_id).first()
    result = Task.query.filter_by(task_id=task_id).first()

    if result:
        json_result = {
            'task_id': result.task_id,
            'task name': result.name,
            'due date': str(result.due_date),
            'priority': result.priority,
            'posted date': str(result.posted_date),
            'status': result.status,
            'user_id': result.user_id
        }
        status_code =200
    else:
        json_result = {'error': 'Element does not exists'}
        status_code = 404

    # geef het json object, samen met de juiste statuscode terug
    return make_response(jsonify(json_result), status_code)