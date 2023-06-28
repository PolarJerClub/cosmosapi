from flask import Blueprint, request, jsonify
from cosmos.helpers import token_required
from cosmos.models import db, Cosmos, cosmo_schema, cosmos_schema

api = Blueprint('api', __name__, url_prefix='/api')



@api.route('/getdata')
def getdata():
    return {'some': 'value'}

#Create Cosmos Endpoint
@api.route('/cosmos', methods=['POST'])
@token_required
def create_cosmo(our_user):

    name = request.json['name']
    mass = request.json['mass']
    radius = request.json['radius']
    period = request.json['period']
    semi_major_axis = request.json['semi_major_axis']
    temperature = request.json['temperature']
    distance_light_year = request.json['distance_light_year']
    host_star_mass = request.json['host_star_mass']
    host_star_temperature = request.json['host_star_temperature']
    random_joke = "" # come back and add this shit
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    cosmo = Cosmos(name, mass, radius, period, semi_major_axis, temperature, distance_light_year, host_star_mass, 
                host_star_temperature, random_joke, user_token)
    
    db.session.add(cosmo)
    db.session.commit()

    response = cosmo_schema.dump(cosmo)

    return jsonify(response)

# Read 1 single cosmo Endpoint
@api.route('/cosmos/<id>', methods=['GET'])
@token_required
def get_cosmo(our_user, id):
    if id:
        cosmo = Cosmos.query.get(id)
        response = cosmo_schema.dump(cosmo)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401
    
# Read all cosmos
@api.route('/cosmos', methods = ['GET'])
@token_required
def get_cosmos(our_user):
    token = our_user.token
    cosmos = Cosmos.query.filter_by(user_token = token).all()
    response = cosmos_schema.dump(cosmos)

    return jsonify(response)


# Update 1 cosmo by id
@api.route('/cosmos/<id>', methods = ['PUT'])
@token_required
def update_cosmo(our_user, id):
    cosmo = Cosmos.query.get(id)

    cosmo.name = request.json['name']
    cosmo.mass = request.json['mass']
    cosmo.radius = request.json['radius']
    cosmo.period = request.json['period']
    cosmo.semi_major_axis = request.json['semi_major_axis']
    cosmo.temperature = request.json['temperature']
    cosmo.distance_light_year = request.json['distance_light_year']
    cosmo.host_star_mass = request.json['host_star_mass']
    cosmo.host_star_temperature = request.json['host_star_temperature']
    cosmo.random_joke = "" # come back and add this shit
    cosmo.user_token = our_user.token

    db.session.commit()

    response = cosmo_schema.dump(cosmo)

    return jsonify(response)


# Delete 1 cosmo by id
@api.route('/cosmos/<id>', methods = ['DELETE'])
@token_required
def delete_cosmo(our_user, id):
    cosmo = Cosmos.query.get(id)
    db.session.delete(cosmo)
    db.session.commit()

    response = cosmo_schema.dump(cosmo)

    return jsonify(response)