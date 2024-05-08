from courier_api import CourierApi
import helper
import allure


class TestLoginCourier:
    @allure.title('Проверка успешности авторизации курьера')
    def test_success_login_courier(self, log_courier):
        response = CourierApi.login_courier(log_courier)
        id_courier = response.json()['id']
        assert response.status_code == 200 and id_courier is not None

    @allure.title('Проверка ошибки при попытке авторизоваться без поля login')
    def test_login_courier_empty_login(self, log_courier):
        mod_payload = helper.ModifyData.modify_login_courier_body(log_courier, "login", "")
        response = CourierApi.login_courier(mod_payload)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при попытке авторизоваться без поля password')
    def test_login_courier_empty_password(self, log_courier):
        new_payload = helper.ModifyData.modify_login_courier_body(log_courier, "password", "")
        response = CourierApi.login_courier(new_payload)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при попытке авторизоваться под несуществующим пользователем ')
    def test_login_courier_invalid_data(self, log_courier):
        invalid_login = log_courier["login"][0:9]
        invalid_password = log_courier["password"][0:9]
        mod_payload = helper.ModifyData.modify_login_courier_body(log_courier, "login", invalid_login)
        new_payload = helper.ModifyData.modify_login_courier_body(mod_payload, "password", invalid_password)
        response = CourierApi.login_courier(new_payload)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.text
