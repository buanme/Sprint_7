import random
import string


class Urls:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/'
    ORDERS = '/api/v1/orders'


class RandomString:

    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def login_pass():
        # генерируем логин, пароль и имя курьера
        login = RandomString.generate_random_string(10)
        password = RandomString.generate_random_string(10)
        first_name = RandomString.generate_random_string(10)

        # собираем тело запроса
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return data
