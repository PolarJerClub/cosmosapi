from flask import Blueprint, render_template


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('look at this shizzle myu nizzle')
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')