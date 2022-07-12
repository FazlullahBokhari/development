# forms.py owners
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField

class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner: ')
    puppy_id = IntegerField("Puppy ID : ")
    submit = SubmitField('Add Owner')
