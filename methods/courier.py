import allure
import requests

from data import Urls


class Courier:
    @staticmethod
    @allure.step("Метод создания курьера")
    def create_courier(login, password, first_name):
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

    @staticmethod
    @allure.step("Метод авторизации курьера")
    def login_courier(login, password):
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

    @staticmethod
    @allure.step("Метод удаления курьера")
    def delete_courier(id_courier):
        response = requests.delete(f'{Urls.BASE_URL}{Urls.DELETE_COURIER}{id_courier}')
        return response.json()
