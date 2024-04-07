from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL 

class AddPet(FlaskForm):
    
    name = StringField("Name" , validators=[InputRequired(message="Cant be blank")])
    species= SelectField("Species", choices=[('dog','dog'),('cat','cat'),('porcupine','porcupine')])
    photo_url= StringField("Photo URL", validators=[Optional(),URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0,max=30)])
    notes = StringField("Notes")


class EditPet(FlaskForm):
    
    photo_url= StringField("Photo URL", validators=[Optional(),URL()])
    notes = StringField("Notes")
    available = BooleanField("Available")    