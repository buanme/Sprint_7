import allure

from data import RandomString, Responses


class TestLoginCouriers:
    @allure.title("Проверка, что при авторизации курьера, запрос возвращает id")
    def test_login_courier_success(self, courier):
        login_pass = RandomString.login_pass()
        courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        assert "id" in login_courier["response"] and login_courier["response"]["id"] > 0
        courier.delete_courier(login_courier["response"]["id"])

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке авторизоваться с неверным логином")
    def test_login_courier_with_incorrect_login_error(self, courier):
        login_pass = RandomString.login_pass()
        courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        login_courier = courier.login_courier(login_pass["login"]+"1", login_pass["password"])
        assert login_courier["status_code"] == 404 and login_courier["response"]["message"] == Responses.COURIER_NOT_FOUND
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        courier.delete_courier(login_courier["response"]["id"])

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке авторизоваться с неверным паролем")
    def test_login_courier_with_incorrect_password_error(self, courier):
        login_pass = RandomString.login_pass()
        courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"]+"1")
        assert login_courier["status_code"] == 404 and login_courier["response"]["message"] == Responses.COURIER_NOT_FOUND
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        courier.delete_courier(login_courier["response"]["id"])

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке авторизоваться без логина")
    def test_login_courier_without_login_error(self, courier):
        login_pass = RandomString.login_pass()
        courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        login_courier = courier.login_courier("", login_pass["password"])
        assert login_courier["status_code"] == 400 and login_courier["response"]["message"] == Responses.COURIER_AUTH_ERROR_IN_DATA
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        courier.delete_courier(login_courier["response"]["id"])

    @allure.title("Проверка, что приходят верные статус код и сообщение при попытке авторизоваться без пароля")
    def test_login_courier_without_password_error(self, courier):
        login_pass = RandomString.login_pass()
        courier.create_courier(login_pass["login"], login_pass["password"], login_pass["firstName"])
        login_courier = courier.login_courier(login_pass["login"], "")
        assert login_courier["status_code"] == 400 and login_courier["response"]["message"] == Responses.COURIER_AUTH_ERROR_IN_DATA
        login_courier = courier.login_courier(login_pass["login"], login_pass["password"])
        courier.delete_courier(login_courier["response"]["id"])
