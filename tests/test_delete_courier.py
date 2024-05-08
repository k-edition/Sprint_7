from courier_api import CourierApi
import allure


class TestDeleteCourier:
    @allure.title('Проверка успешности удаления курьера')
    def test_success_delete_courier(self, default_courier):
        response = CourierApi.delete_courier(default_courier)
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверка ошибки при удалении курьера без указания id')
    def test_delete_courier_without_id(self):
        response = CourierApi.delete_courier_without_id()
        assert response.status_code == 400

    @allure.title('Проверка ошибки при удалении курьера с несуществующим id')
    def test_delete_courier_by_invalid_id(self, default_courier):
        invalid_id = default_courier+999
        response = CourierApi.delete_courier(invalid_id)
        assert response.status_code == 404 and "Курьера с таким id нет" in response.text
