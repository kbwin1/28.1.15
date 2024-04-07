from models import db, Pet
from app import app

db.drop_all()
db.create_all()

pet1=Pet(name='rock',species="dog", photo_url='https://cdn.britannica.com/69/234469-050-B883797B/Rottweiler-dog.jpg?w=400&h=300&c=crop',age=1,notes="good boy",available=True)

db.session.add(pet1)
db.session.commit()