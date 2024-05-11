from courier_api import CourierApi
import helper
import allure


class TestLoginCourier:
    @allure.title('Проверка успешности авторизации курьера')
    def test_success_login_courier(self, make_courier, remove_courier):
        new_payload = helper.ModifyData.modify_payload_for_login_courier(make_courier)
        response = CourierApi.login_courier(new_payload)
        id_courier = response.json()['id']
        remove_courier(id_courier)
        assert response.status_code == 200 and id_courier is not None

    @allure.title('Проверка ошибки при попытке авторизоваться без поля login')
    def test_login_courier_empty_login(self, make_courier, auth_courier, remove_courier):
        mod_payload = helper.ModifyData.modify_login_courier_body(make_courier, "login", "")
        response = CourierApi.login_courier(mod_payload)
        id_courier = auth_courier(make_courier)
        remove_courier(id_courier)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при попытке авторизоваться без поля password')
    def test_login_courier_empty_password(self, make_courier, auth_courier, remove_courier):
        new_payload = helper.ModifyData.modify_login_courier_body(make_courier, "password", "")
        response = CourierApi.login_courier(new_payload)
        id_courier = auth_courier(make_courier)
        remove_courier(id_courier)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при попытке авторизоваться под несуществующим пользователем ')
    def test_login_courier_invalid_data(self, make_courier, auth_courier, remove_courier):
        invalid_login = make_courier["login"][0:9]
        invalid_password = make_courier["password"][0:9]
        mod_payload = helper.ModifyData.modify_login_courier_body(make_courier, "login", invalid_login)
        new_payload = helper.ModifyData.modify_login_courier_body(mod_payload, "password", invalid_password)
        response = CourierApi.login_courier(new_payload)
        id_courier = auth_courier(make_courier)
        remove_courier(id_courier)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.text
