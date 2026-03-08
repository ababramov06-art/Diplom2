import pytest
import allure
import requests
from urls import *
from data import *
from methods import RegMethod
from methods import OrderMethod


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

    yield payload_cred
    access_token = response_body['accessToken']
    RegMethod.delete_user(access_token)

@pytest.fixture
@allure.step('Фикстура создает пользователя и заказ для его аккаунта')
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [IngredientData.burger_2]}
    OrderMethod.create_order(payload, headers)
    
    yield access_token, response_body

    RegMethod.delete_user(access_token)
