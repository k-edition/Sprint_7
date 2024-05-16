import requests
import urls
import allure


class OrderApi:
    @staticmethod
    @allure.step("Отправляем запрос POST на создание заказа")
    def create_order(payload):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправляем запрос GET на получение списка заказов")
    def get_order_list():
        return requests.get(urls.BASE_URL + urls.GET_LIST_ORDER_ENDPOINT)

    @staticmethod
    @allure.step("Отправляем запрос GET на получение заказа по его номеру")
    def get_order(id_track):
        query_param = f't={id_track}'
        return requests.get(urls.BASE_URL + urls.GET_ORDER_ENDPOINT + '?' + query_param)

    @staticmethod
    @allure.step("Отправляем запрос GET на получение заказа без указания номера")
    def get_order_without_track():
        return requests.get(urls.BASE_URL + urls.GET_ORDER_ENDPOINT)

    @staticmethod
    @allure.step("Отправляем запрос PUT на принятие заказа")
    def accept_order(order_id, id_courier):
        query_param = f'courierId={id_courier}'
        return requests.put(urls.BASE_URL + urls.ACCEPT_ORDER_ENDPOINT + f'{order_id}' + '?' + query_param)
