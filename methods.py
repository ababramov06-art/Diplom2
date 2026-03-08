import requests
from urls import Urls
import allure


class RegMethod:
    @allure.step('Создание пользователя')
    def create_user(body):
        return requests.post(Urls.user_register, json=body)
    
    @allure.step('Удаление пользователя')
    def delete_user(access_token):
        return requests.delete(Urls.user_delete, headers={'Authorization': access_token})

class AuthMethod:
    @allure.step('Регистрация пользователя')
    def auth_user(body):
        return requests.post(Urls.user_auth, json=body)
    
class OrderMethod:
    @allure.step('Создание заказ')
    def create_order(body, headers):
        return requests.post(Urls.order_create, json=body, headers=headers)