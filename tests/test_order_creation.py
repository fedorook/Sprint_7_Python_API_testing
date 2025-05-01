import pytest
import requests
from config import BASE_URL, ORDER

@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def test_create_order_with_color(color):
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }
    response = requests.post(f"{BASE_URL}{ORDER}", json=order_data)
    assert response.status_code == 201
    assert 'track' in response.json()