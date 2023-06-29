from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from cosmos.forms import CosmoForm
from cosmos.models import Cosmos, db
# from cosmos.helpers import random_joke_generator


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
            mass = cosmoform.mass.data
            radius = cosmoform.radius.data
            period = cosmoform.period.data
            semi_major_axis = cosmoform.semi_major_axis.data
            temperature = cosmoform.temperature.data
            distance_light_year = cosmoform.distance_light_year.data
            host_star_mass = cosmoform.host_star_mass.data
            host_star_temperature = cosmoform.host_star_temperature.data
            # if droneform.dad_joke.data:
            #     random_joke = droneform.dad_joke.data
            # else:
            #     random_joke = random_joke_generator()
            user_token = current_user.token

            cosmo = Cosmos(name, mass, radius, period, semi_major_axis, temperature, 
                          distance_light_year, host_star_mass, host_star_temperature, user_token)
            
            db.session.add(cosmo)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Planet not created, please check your form and try again.')

    user_token = current_user.token
    cosmos = Cosmos.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=cosmoform, cosmos=cosmos)