import pytest
import allure
import requests
from urls import *
from data import *
from methods import RegMethod
from methods import OrderMethod
from helpers import create_random_username, create_random_email, create_random_password

@pytest.fixture
@allure.step('Фикстура создает пользователя с рандомными кредами и удаляет его из базы после теста')
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }
    response = RegMethod.create_user(payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    RegMethod.delete_user(access_token)

