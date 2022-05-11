from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    diameter_in_km = db.Column(db.Integer)
    


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