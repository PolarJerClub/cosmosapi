from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit_button = SubmitField()  

class CosmoForm(FlaskForm):
    name = StringField('name')
    # mass = DecimalField('mass', places=10)
    # radius = DecimalField('radius', places=10)
    # period = DecimalField('period', places=10)
    # semi_major_axis = DecimalField('semi major axis', places=10)
    # temperature = DecimalField('temperature', places=10)
    # distance_light_year = DecimalField('distance light year', places=10)
    # host_star_mass = DecimalField('host star mass', places=10)
    # host_star_temperature = DecimalField('host star temperature', places=10)
    submit_button = SubmitField()