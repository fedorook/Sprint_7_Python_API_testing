import requests
import random
from conftest import courier_data
from config import BASE_URL, COURIER


class TestCourierCreation:
    def test_create_courier_success(self, courier_data):
        data = {
            "login": 'test_login_' + str(random.randint(1, 100000)),
            "password": 'test_password_' + str(random.randint(1, 100000)),
            "firstName": 'test_name_' + str(random.randint(1, 100000))
        }
        response = requests.post(f"{BASE_URL}{COURIER}", data=data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self, courier_data):
        login, password, first_name = courier_data
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
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