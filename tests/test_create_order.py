from order_api import OrderApi
import pytest
import allure
import helper


class TestCreateOrder:

    colors = [["BLACK"], ["GREY"], ["BLACK", "GREY"], None]

    @pytest.mark.parametrize('color', colors)
    @allure.title('Проверка успешности создания заказа')
    def test_success_create_order(self, color):
        payload = helper.ModifyData.modify_create_order_body("color", color)
        response = OrderApi.create_order(payload)
        id_track = response.json()["track"]
        assert response.status_code == 201 and id_track is not None
