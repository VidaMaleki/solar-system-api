from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    return app

class Book:
    def __init__(self, id, title, description, author):
        self.id = id
        self.title = title
        self.description = description
        self.author = author