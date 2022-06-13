# project/tasks/forms.py

# Docs: https://wtforms.readthedocs.io/en/3.0.x/

# from flask_wtf import Form, FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional
# Email validator needs add-on package: pip install wtforms[email]



class AddTaskForm(FlaskForm):
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField('Due Date (mm/dd/yyyy)', validators=[Optional()], format='%Y-%m-%d')
    priority = SelectField(
        'Priority',
        validators=[DataRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
            ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
        ]
    )
    status = IntegerField('Status')

