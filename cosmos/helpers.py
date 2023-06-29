from flask import request, jsonify
from functools import wraps
import secrets
import decimal
import requests
import json

from cosmos.models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        """
        This functino takes in any number of args & kwargs and verifies
        that the token passed into the headers is associated with a 
        user in the database
        """
        
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split()[1]
            print(token)

        if not token:
            return jsonify({'message': 'Token is missing'}), 401 #client error
        
        try:
            our_user = User.query.filter_by(token=token).first()
            print(our_user)
            if not our_user or our_user.token != token:
                return jsonify({'message': 'Token is invalid'}), 401 #client error
            
        except:
            our_user = User.query.filter_by(token=token).first()
            if token != our_user.token and secrets.compare_digest(token, our_user.token):
                return jsonify({'message': 'Token is invalid'}), 401
        
        return our_flask_function(our_user, *args, **kwargs)
    
    return decorated


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj)
    

def planet_generator(planet):
    url = "https://planets-by-api-ninjas.p.rapidapi.com/v1/planets"

    querystring = {"name":planet}

    headers = {
        "X-RapidAPI-Key": "0b0505dffemshaa450b6c1ffa423p17b6cfjsn660a4103b1ce",
        "X-RapidAPI-Host": "planets-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    return data
    

# def star_generator():
#     url = "https://stars-by-api-ninjas.p.rapidapi.com/v1/stars"

#     querystring = {"name":"vega"}

#     headers = {
#         "X-RapidAPI-Key": "0b0505dffemshaa450b6c1ffa423p17b6cfjsn660a4103b1ce",
#         "X-RapidAPI-Host": "stars-by-api-ninjas.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     data = response.json()

#     return data