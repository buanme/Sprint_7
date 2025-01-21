import random
import string


class Urls:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/'
    ORDERS = '/api/v1/orders'
    CANCEL_ORDER = '/api/v1/orders/cancel'


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


class Responses:
    NEW_COURIER_CREATE = {'ok': True}
    COURIER_CREATE_WITH_SAME_NAME = 'Этот логин уже используется'
    NEW_COURIER_ERROR_IN_DATA = 'Недостаточно данных для создания учетной записи'
    COURIER_NOT_FOUND = 'Учетная запись не найдена'
    COURIER_AUTH_ERROR_IN_DATA = 'Недостаточно данных для входа'

    ORDER_EXAMPLES = [({"first_name": "Заказ",
                                      "last_name": "Тестовый",
                                      "address": "Москва",
                                      "station": "4",
                                      "phone": "+7 800 355 35 35",
                                      "rent_time": "5",
                                      "date": "2025-06-06",
                                      "comment": "тестовое создание заказа",
                                      "color": ["BLACK"]}),
                                    ({"first_name": "Заказ",
                                      "last_name": "Тестовый",
                                      "address": "Москва",
                                      "station": "4",
                                      "phone": "+7 800 355 35 35",
                                      "rent_time": "5",
                                      "date": "2025-06-06",
                                      "comment": "тестовое создание заказа",
                                      "color": ["GREY"]}),
                                     ({"first_name": "Заказ",
                                       "last_name": "Тестовый",
                                       "address": "Москва",
                                       "station": "4",
                                       "phone": "+7 800 355 35 35",
                                       "rent_time": "5",
                                       "date": "2025-06-06",
                                       "comment": "тестовое создание заказа",
                                       "color": ["BLACK", "GREY"]}),
                                     ({"first_name": "Заказ",
                                       "last_name": "Тестовый",
                                       "address": "Москва",
                                       "station": "4",
                                       "phone": "+7 800 355 35 35",
                                       "rent_time": "5",
                                       "date": "2025-06-06",
                                       "comment": "тестовое создание заказа",
                                       "color": []})
                                     ]