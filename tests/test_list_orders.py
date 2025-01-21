import allure


class TestListOrder:
    @allure.title("Проверка, что в тело ответа возвращается список заказов")
    def test_get_list_orders_success(self, order):
        list_orders = order.get_list_orders()
        assert list_orders["status_code"] == 200 and "orders" in list_orders["response"] and isinstance(list_orders["response"]["orders"], list)
