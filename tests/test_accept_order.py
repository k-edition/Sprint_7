from order_api import OrderApi
import allure


class TestAcceptOrder:
    @allure.title('Проверка успешности принятия заказа')
    def test_success_accept_order(self, order_id, make_courier, auth_courier, remove_courier):
        id_courier = auth_courier(make_courier)
        response = OrderApi.accept_order(order_id, id_courier)
        remove_courier(id_courier)
        assert response.status_code == 200 and response.text == '{"ok":true}'
