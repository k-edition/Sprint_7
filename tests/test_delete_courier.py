from courier_api import CourierApi
import allure


class TestDeleteCourier:
    @allure.title('Проверка успешности удаления курьера')
    def test_success_delete_courier(self, make_courier, auth_courier):
        id_courier = auth_courier(make_courier)
        response = CourierApi.delete_courier(id_courier)
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверка ошибки при удалении курьера без указания id')
    def test_delete_courier_without_id(self):
        response = CourierApi.delete_courier_without_id()
        assert response.status_code == 400

    @allure.title('Проверка ошибки при удалении курьера с несуществующим id')
    def test_delete_courier_by_invalid_id(self, make_courier, auth_courier, remove_courier):
        invalid_id = auth_courier(make_courier)+999
        response = CourierApi.delete_courier(invalid_id)
        id_courier = auth_courier(make_courier)
        remove_courier(id_courier)
        assert response.status_code == 404 and "Курьера с таким id нет" in response.text
