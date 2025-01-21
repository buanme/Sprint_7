import json

import allure
import requests

from data import Urls


class Orders:

    @allure.step("Метод создания заказа")
    def create_order(self, data):
        # собираем тело запроса
        payload = {
            "firstName": data["first_name"],
            "lastName": data["last_name"],
            "address": data["address"],
            "metroStation": data["station"],
            "phone": data["phone"],
            "rentTime": data["rent_time"],
            "deliveryDate": data["date"],
            "comment": data["comment"],
            "color": data["color"]
        }
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS}', data=json.dumps(payload))

        order = {
            "status_code": response.status_code,
            "response": response.json()
        }
        # возвращаем список
        return order

    @allure.step("Метод получения списка заказов")
    def get_list_orders(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS}')
        orders = {
            "status_code": response.status_code,
            "response": response.json() if response.status_code == 200 else response.text
        }
        return orders

    @allure.step("Метод отмены заказа")
    def put_cancel_order(self, track):
        response = requests.put(f'{Urls.BASE_URL}{Urls.CANCEL_ORDER}?track={track}')
        order = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return order
