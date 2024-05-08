from order_api import OrderApi
import allure


class TestGetOrder:
    @allure.title('Проверка успешности получения заказа по его номеру')
    def test_success_get_order(self, default_order):
        response = OrderApi.get_order(default_order)
        assert response.status_code == 200 and response.json()['order']['track'] == default_order

    @allure.title('Проверка ошибки при попытке получения заказа с несуществующим номером')
    def test_get_order_by_invalid_track(self, default_order):
        invalid_track = default_order + 999999
        response = OrderApi.get_order(invalid_track)
        assert response.status_code == 404 and "Заказ не найден" in response.text

    @allure.title('Проверка ошибки при попытке получения заказа без указания номера')
    def test_get_order_without_track(self):
        response = OrderApi.get_order_without_track()
        assert response.status_code == 400
