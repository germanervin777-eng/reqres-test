import allure
from utils.http_methods import HttpMethods
from utils.logger import Logger

class ReqResApi:
    def __init__(self):
        self.base_url = "https://reqres.in/api"

    @allure.step("Создание пользователя")
    def create_user(self, payload):
        url = f"{self.base_url}/users"
        Logger.add_request(url, "POST", body=payload)
        resp = HttpMethods.post(url, json_body=payload)
        Logger.add_response(resp)
        return resp

    @allure.step("Получение пользователя")
    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        Logger.add_request(url, "GET")
        resp = HttpMethods.get(url)
        Logger.add_response(resp)
        return resp

    @allure.step("Обновление пользователя")
    def update_user(self, user_id, payload):
        url = f"{self.base_url}/users/{user_id}"
        Logger.add_request(url, "PUT", body=payload)
        resp = HttpMethods.put(url, json_body=payload)
        Logger.add_response(resp)
        return resp

    @allure.step("Удаление пользователя")
    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        Logger.add_request(url, "DELETE")
        resp = HttpMethods.delete(url)
        Logger.add_response(resp)
        return resp