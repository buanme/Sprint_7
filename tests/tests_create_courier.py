import allure

from data import RandomString


class TestCreateCouriers:
    @allure.title("Проверка, что приходят верные статус код и тело ответа при создании курьера")
    def test_create_courier_success(self, courier):
        login_pass = RandomString.login_pass()
        new_courier = courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        assert new_courier["status_code"] == 201 and new_courier["response"] == {'ok': True}
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        courier.delete_courier(login_courier["response"]["id"])

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке создать двух одинаковых курьеров")
    def test_create_couriers_with_same_name_error(self, courier):
        login_pass = RandomString.login_pass()
        new_courier = courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        courier_with_same_name = courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        assert courier_with_same_name["status_code"] == 409 and courier_with_same_name["response"]["message"] == "Этот логин уже используется"
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        courier.delete_courier(login_courier["response"]["id"])

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке создать курьера без логина")
    def test_create_courier_without_login_error(self, courier):
        login_pass = RandomString.login_pass()
        new_courier = courier.create_courier("", login_pass["password"], login_pass["firstName"])
        assert new_courier["status_code"] == 400 and new_courier["response"]["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке создать курьера без паспорта")
    def test_create_courier_without_password_error(self, courier):
        login_pass = RandomString.login_pass()
        new_courier = courier.create_courier(login_pass["login"], "", login_pass["firstName"])
        assert new_courier["status_code"] == 400 and new_courier["response"]["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке создать курьера без имени")
    def test_create_courier_without_first_name_error(self, courier):
        login_pass = RandomString.login_pass()
        new_courier = courier.create_courier(login_pass["login"], login_pass["password"], "")
        assert new_courier["status_code"] == 400 and new_courier["response"]["message"] == "Недостаточно данных для создания учетной записи"
