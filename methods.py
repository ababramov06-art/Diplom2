import requests
from urls import Urls

class RegMethod:
    def create_user(body):
        return requests.post(Urls.user_register, json=body)

class AuthMethod:
    def auth_user(body):
        return requests.post(Urls.user_auth, json=body)
    
class OrderMethod:
    def create_order(body, headers):
        return requests.post(Urls.order_create, json=body, headers=headers)