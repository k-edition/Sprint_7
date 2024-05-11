import pytest
import data
import helper
from courier_api import CourierApi
from order_api import OrderApi


@pytest.fixture(scope='function')
def get_payload():
    payload = data.generate_payload_for_create_courier()
    return payload


@pytest.fixture(scope='function')
def make_courier(get_payload):
    CourierApi.create_courier(get_payload)
    return get_payload


@pytest.fixture(scope='function')
def auth_courier(request):
    def _auth_courier(payload):
        new_payload = helper.ModifyData.modify_payload_for_login_courier(payload)
        login_response = CourierApi.login_courier(new_payload)
        id_courier = login_response.json()['id']
        return id_courier
    return _auth_courier


@pytest.fixture(scope='function')
def remove_courier(request):
    def _remove_courier(id_courier):
        CourierApi.delete_courier(id_courier)
    return _remove_courier


@pytest.fixture(scope='function')
def default_order():
    payload = data.generate_payload_for_create_order()
    response = OrderApi.create_order(payload)
    id_track = response.json()["track"]
    return id_track


@pytest.fixture(scope='function')
def order_id():
    payload = data.generate_payload_for_create_order()
    response = OrderApi.create_order(payload)
    id_track = response.json()["track"]
    second_response = OrderApi.get_order(id_track)
    return second_response.json()['order']['id']
