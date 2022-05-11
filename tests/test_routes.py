
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_list_of_planets(client,three_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 5,
            "name": "Mercury",
            "description": "the fastest planet",
            "diameter_in_km": 4879
            },
        {
            "id": 6,
            "name": "Venus",
            "description": "the brightest planet",
            "diameter_in_km": 12104
            },
        {
            "id": 3,
            "name": "Mandy&Vida",
            "description": "Ada C17 planet",
            "diameter_in_km": 1234
            }
        ]


def test_get_one_planet(client, three_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "the fastest planet",
        "diameter_in_km": 4879
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "our own planet!",
        "diameter_in_km": 12756
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {'id': 1}