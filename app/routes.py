from flask import Blueprint, jsonify, request
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

# def get_all_planets():
#     response = []
#     for planet in planets:
#         response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "diameter_in_km": planet.diameter_in_km
#             }
#         )
#     return jsonify(response)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return jsonify({'message': f"Invalid Planet ID: {planet_id} must be an interger"}), 400 #string input
#     chosen_planet = None
#     for planet in planets:
#         if planet.id == planet_id:
#             chosen_planet = {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "diameter_in_km": planet.diameter_in_km
#             }
#     if chosen_planet is None:
#         return jsonify({'message': f"Could not find planet with {planet_id}"}), 404 #ID not in dict
#     return jsonify(chosen_planet)


