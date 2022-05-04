from calendar import c
from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.planets import Planet

# class Planet():
#         def __init__(self, id, name, description,diameter_in_km):
#             self.id = id
#             self.name = name
#             self.description = description
#             self.diameter_in_km = diameter_in_km

# planets = [
#     Planet(11,"Mercury", "the fastest planet", 4879),
#     Planet(22,"Venus", "the brightest planet", 12104),
#     Planet(33,"Earth", "our own planet", 12756),
#     Planet(44,"Mars", "the red planet", 6792),
#     Planet(66,"Jupiter", "the largest planet", 142984),
#     Planet(77,"Saturn", "the slowest planet", 120536),
#     Planet(88,"Uranus", "named after the Greek god of the sky", 51118),
#     Planet(99,"Neptune", "a deep sea-blue colour", 49528)
#     ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()
    print(request_body)
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        diameter_in_km = request_body["diameter_in_km"])

    db.session.add(new_planet)
    db.session.commit()
    
    return {
        "id": new_planet.id
    }, 201

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    params = request.args
    if "name" in params and "description" in params:
        name_value = params["name"]
        description_value = params["description"]
        planets = Planet.query.filter_by(name = name_value, description = description_value)
    elif "name" in params:
        name_value = params["name"]
        planets = Planet.query.filter_by(name = name_value)
    elif "description" in params:
        description_value = params["description"]
        planets = Planet.query.filter_by(description = description_value)
    
    else:
        planets = Planet.query.all()
    response = []
    for planet in planets:
        response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter_in_km": planet.diameter_in_km
        })

    return jsonify(response)

def get_planet_or_abort(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = ({'message': f"Invalid Planet ID: {planet_id} must be an interger"})
        abort(make_response(jsonify(response), 400)) #string input
        
    request_body = request.get_json()
    # if "name" not in request_body or "description" not in request_body or "diameter_in_km" not in request_body:
    #         return jsonify({'message': "Request must include name, description, and diameter_in_km"}), 400
    
    chosen_planet = Planet.query.get(planet_id)
    if chosen_planet is None:
        response = ({'message': f"Could not find planet with {planet_id}"})
        abort(make_response(jsonify(response), 404))
        
    return chosen_planet

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):

    chosen_planet = get_planet_or_abort(planet_id)
    chosen_planet = {
        "id": chosen_planet.id,
        "name": chosen_planet.name,
        "description": chosen_planet.description,
        "diameter_in_km": chosen_planet.diameter_in_km
    }

    return jsonify(chosen_planet)


@planets_bp.route("/<planet_id>", methods = ["PUT"])
def replace_one_planet(planet_id):
    request_body = request.get_json()
    chosen_planet = get_planet_or_abort(planet_id)
    chosen_planet.name = request_body["name"]
    chosen_planet.description = request_body["description"]
    chosen_planet.diameter_in_km = request_body["diameter_in_km"]
    
    db.session.commit()
    
    return jsonify({'message': f"Successfully replaced planet with id{planet_id}"})

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_one_planet(planet_id):
    #request_body = request.get_json()
    chosen_planet = get_planet_or_abort(planet_id)
    
    db.session.delete(chosen_planet)
    db.session.commit()
    
    return jsonify({'message': f"Deleted planet with id {planet_id}"})