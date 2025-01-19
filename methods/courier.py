import requests

from data import Urls


class Courier:
    # метод создания курьера
    def create_courier(self, login, password, first_name):
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_COURIER}', data=payload)

        courier = {
            "status_code": response.status_code,
            "response": response.json()
        }
        # возвращаем список
        return courier

    def login_courier(self, login, password):
        courier = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', data=courier)

        login_courier = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return login_courier

    def delete_courier(self, id_courier):
        response = requests.delete(f'{Urls.BASE_URL}{Urls.DELETE_COURIER}{id_courier}')
        delete_courier = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return response.json()
