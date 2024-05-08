import requests
import urls
import allure


class CourierApi:
    @staticmethod
    @allure.step("Отправляем запрос POST на создание курьера")
    def create_courier(payload):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправляем запрос POST на логин курьера")
    def login_courier(payload):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправляем запрос DELETE на удаление курьера")
    def delete_courier(id_courier):
        return requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(id_courier))

    @staticmethod
    @allure.step("Отправляем запрос DELETE на удаление курьера без указания id")
    def delete_courier_without_id():
        return requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT)
