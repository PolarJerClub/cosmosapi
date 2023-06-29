from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from cosmos.forms import CosmoForm
from cosmos.models import Cosmos, db
from cosmos.helpers import planet_generator


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('look at this shizzle muy nizzle')
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    cosmoform = CosmoForm()

    try:
        if request.method == 'POST' and cosmoform.validate_on_submit():
            name = cosmoform.name.data
            # if droneform.dad_joke.data:
            #     random_joke = droneform.dad_joke.data
            # else:
            #     random_joke = random_joke_generator()

            # mass, radius, period, semi_major_axis, temperature, 
            #               distance_light_year, host_star_mass, host_star_temperature,
            user_token = current_user.token

            data = planet_generator(name)
            mass = data[0]['mass']
            radius = data[0]['radius']
            period = data[0]['period']
            semi_major_axis = data[0]['semi_major_axis']
            temperature = data[0]['temperature']
            distance_light_year = data[0]['distance_light_year']
            host_star_mass = data[0]['host_star_mass']
            host_star_temperature = data[0]['host_star_temperature']

            cosmo = Cosmos(name, mass, radius, period, semi_major_axis, temperature, distance_light_year,
                           host_star_mass, host_star_temperature, user_token)
            
            db.session.add(cosmo)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Planet not created, please check your form and try again.')

    user_token = current_user.token
    cosmos = Cosmos.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=cosmoform, cosmos=cosmos)