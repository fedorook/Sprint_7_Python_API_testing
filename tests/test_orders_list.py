import requests

def test_get_orders_list():
    response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
    assert response.status_code == 200
    assert isinstance(response.json()['orders'], list)