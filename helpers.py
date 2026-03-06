from faker import Faker
import allure

fake = Faker()
fakeRU = Faker(locale='ru_RU')

@allure.step("Генерация случайного email")
def create_random_email():
    email = fake.free_email()
    return email

@allure.step("Генерация случайного пароля длиной 10 символов")
def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password

@allure.step("Генерация случайного имени пользователя")
def create_random_username():
    username = fakeRU.first_name()
    return username
