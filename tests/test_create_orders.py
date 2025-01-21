import allure
import pytest

from data import Responses


class TestCreateOrder:
    @allure.title("Проверка, что при создании заказа запрос имеет верный статус код и возвращает track")
    @pytest.mark.parametrize("data",Responses.ORDER_EXAMPLES)
    def test_create_order_success(self, order, data):
        create_order = order.create_order(data)
        assert create_order["status_code"] == 201 and "track" in create_order["response"]
        order.put_cancel_order(create_order["response"]["track"])
