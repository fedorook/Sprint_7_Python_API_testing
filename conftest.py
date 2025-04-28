import pytest
from tests.utils import register_new_courier_and_return_login_password

@pytest.fixture
def courier_data():
    return register_new_courier_and_return_login_password()