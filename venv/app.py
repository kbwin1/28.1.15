from flask import Flask, request, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet
from forms import AddPet, EditPet
from flask import abort

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pepe1@localhost/pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] ='lolo'

connect_db(app)
app.app_context().push()

@app.route('/')
def home_page():
    pets=Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route('/add_new_pet', methods=["GET","POST"])
def add_new_pet():
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data  
        species = form.species.data
        photo_url = form.photo_url.data
        age= form.age.data
        notes= form.notes.data
        pet = Pet(name=name,species=species, photo_url=photo_url,age=age,notes=notes,available=True)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:   
       return render_template('add_pet.html',form=form)
   

@app.route('/info/<int:id>',methods=["GET","POST"])
def info(id):
    pet = Pet.query.get_or_404(id)
    form = EditPet(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes= form.notes.data
        pet.available= form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_info.html', form=form,pet=pet) 
    