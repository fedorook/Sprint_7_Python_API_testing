import requests
from config import BASE_URL, ORDER_LIST

def test_get_orders_list():
    response = requests.get(f"{BASE_URL}{ORDER_LIST}")
    assert response.status_code == 200
    assert isinstance(response.json()['orders'], list)