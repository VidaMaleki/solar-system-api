import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planets import Planet


@pytest.fixture
def app():
    app= create_app({"TESTING": True})
    
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
        
    with app.app_context():
        db.create_all()
        yield app
        
    with app.app_context():
        db.drop_all()
        
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_saved_planets(app):
    mercury = Planet(
        name="Mercury",
        description="the fastest planet",
        diameter_in_km= 4879)
    venus = Planet(
            name="Venus",
            description="the brightest planet",
            diameter_in_km= 12104)
    mandy_vida = Planet(
            name= "Mandy&Vida",
            description = "Ada C17 planet",
            diameter_in_km = 1234)
    
    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(mandy_vida)
    
    db.session.commit()