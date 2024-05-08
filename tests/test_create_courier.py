from courier_api import CourierApi
import helper
import allure


class TestCreateCourier:
    @allure.title('Проверка успешности создания курьера')
    def test_success_create_courier(self, new_courier):
        response = CourierApi.create_courier(new_courier)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка ошибки при создании курьера с пустым логином')
    def test_empty_login_create_courier(self):
        mod_payload = helper.ModifyData.modify_create_courier_body("login", "")
        response = CourierApi.create_courier(mod_payload)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при создании курьера с пустым паролем')
    def test_empty_password_create_courier(self):
        mod_payload = helper.ModifyData.modify_create_courier_body("password", "")
        response = CourierApi.create_courier(mod_payload)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при создании курьера с логином, который уже есть')
    def test_create_courier_duplicate(self, new_courier):
        CourierApi.create_courier(new_courier)
        response = CourierApi.create_courier(new_courier)
        assert response.status_code == 409 and "Этот логин уже используется" in response.text
