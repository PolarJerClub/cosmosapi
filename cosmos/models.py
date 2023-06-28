from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime


# Adding Flask Security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import Secrets Module
import secrets

from flask_login import UserMixin, LoginManager

# import for flask-marshmallow
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    username = db.Column(db.String, nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    cosmo = db.relationship('Cosmos', backref = 'owner', lazy = True)

    def __init__(self, email, username, password='', first_name = '', last_name = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token()
        self.username = username

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        return generate_password_hash(password)
    
    def set_token(self):
        return secrets.token_hex(24)
    
    def __repr__(self):
        return f"User {self.email} has been added to the database! :O"
    


class Cosmos(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150))
    mass = db.Column(db.String(200), nullable = True)
    radius = db.Column(db.Numeric(precision=10, scale=2))
    period = db.Column(db.String(150), nullable = True)
    semi_major_axis = db.Column(db.String(100), nullable=True)
    temperature = db.Column(db.String(100))
    distance_light_year = db.Column(db.String(100))
    host_star_mass = db.Column(db.String(100))
    host_star_temperature = db.Column(db.Numeric(precision=10, scale=2))
    random_joke = db.Column(db.String, nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, mass, radius, period, semi_major_axis, temperature, distance_light_year,
                  host_star_mass, host_star_temperature, random_joke, user_token):
        self.id = self.set_id()
        self.name = name
        self.mass = mass
        self.radius = radius
        self.period = period
        self.semi_major_axis = semi_major_axis
        self.temperature = temperature
        self.distance_light_year = distance_light_year
        self.host_star_mass = host_star_mass
        self.host_star_temperature = host_star_temperature
        self.random_joke = random_joke
        self.user_token = user_token

    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f"{self.name} has been added to the database!!! :)"
    

class CosmosSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'mass', 'radius', 'period', 'semi_major_axis', 'temperature',
                  'distance_light_year', 'host_star_mass', 'host_star_temperature', 'random_joke']
        
cosmo_schema = CosmosSchema()
cosmos_schema = CosmosSchema(many = True)