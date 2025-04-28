import requests
import pytest
from conftest import courier_data

class TestCourierLogin:
    def test_courier_login_success(self, courier_data):
        login, password, _ = courier_data
        payload = {"login": login, "password": password}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    def test_courier_login_invalid_password(self, courier_data):
        login, _, _ = courier_data
        payload = {"login": login, "password": "wrong_password"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    def test_login_missing_login_field(self, courier_data):
        _, password, _ = courier_data
        payload = {"password": password}  # Нет логина
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json()['message']

    def test_login_nonexistent_user(self):
        # Генерируем данные, которые точно не были зарегистрированы
        payload = {
            "login": "nonexistent_user_12345",
            "password": "wrong_password_12345"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"