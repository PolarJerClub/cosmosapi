from flask import Flask
from config import Config
from .site.routes import site


app = Flask(__name__)

# @app.route("/") -- simple route on the homepage
# def hello_world():
#     return "<p>Hello World!</p>"

app.register_blueprint(site)

app.config.from_object(Config)