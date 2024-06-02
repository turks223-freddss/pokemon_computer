from . import db
from flask_login import UserMixin


class Pokemon(db.Model,UserMixin):
    poke_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150))
    region = db.Column(db.String(150))
    type1 = db.Column(db.String(150))
    type2 = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pokemon = db.relationship('Pokemon')
    
class Region(db.Model, UserMixin):
    Region_name = db.Column(db.String(150), primary_key=True)
    X_factor = db.Column(db.String(150))
