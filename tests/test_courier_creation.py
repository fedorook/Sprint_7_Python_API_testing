import requests
import random
from conftest import courier_data
from config import BASE_URL, COURIER
from utils import make_courier_payload


class TestCourierCreation:
    def test_create_courier_success(self):
        payload = make_courier_payload()
        response = requests.post(f"{BASE_URL}{COURIER}", data=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self, courier_data):
        login, password, first_name = courier_data
        payload = make_courier_payload(login, password, first_name)
        response = requests.post(f"{BASE_URL}{COURIER}", data=payload)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    def test_create_courier_without_login(self, courier_data):
        _, password, first_name = courier_data
        payload = {
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f"{BASE_URL}{COURIER}", data=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json()['message']