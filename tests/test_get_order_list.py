from order_api import OrderApi
import allure


class TestGetOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        response = OrderApi.get_order_list()
        response_json = response.json()
        assert response.status_code == 200 and response_json["orders"] is not None
