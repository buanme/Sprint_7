import allure
import pytest


class TestCreateOrder:
    @allure.title("Проверка, что при создании заказа запрос имеет верный статус код и возвращает track")
    @pytest.mark.parametrize("data",[({"first_name": "Заказ",
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
                                     ])
    def test_create_order_success(self, order, data):
        create_order = order.create_order(data)
        assert create_order["status_code"] == 201 and "track" in create_order["response"]
