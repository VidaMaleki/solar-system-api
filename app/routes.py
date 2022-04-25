from flask import Blueprint, jsonify

class Planet():
        def __init__(self, id, name, description,diameter_in_km):
            self.id = id
            self.name = name
            self.description = description
            self.diameter_in_km = diameter_in_km

planets = [
    Planet(11,"Mercury", "the fastest planet", 4879),
    Planet(22,"Venus", "the brightest planet", 12104),
    Planet(33,"Earth", "our own planet", 12756),
    Planet(44,"Mars", "the red planet", 6792),
    Planet(66,"Jupiter", "the largest planet", 142984),
    Planet(77,"Saturn", "the slowest planet", 120536),
    Planet(88,"Uranus", "named after the Greek god of the sky", 51118),
    Planet(99,"Neptune", "a deep sea-blue colour", 49528)
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods = ["GET"])

def get_all_planets():
    response = []
    for planet in planets:
        response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "diameter_in_km": planet.diameter_in_km
            }
        )
    return jsonify(response)