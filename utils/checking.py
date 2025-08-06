import allure

class Checking:
    @staticmethod
    @allure.step("Проверка статус-кода")
    def check_status_code(response, expected_status):
        actual = response.status_code
        assert actual == expected_status, f"Ожидался {expected_status}, получили {actual}"

    @staticmethod
    @allure.step("Проверка наличия обязательных полей")
    def check_required_fields(response, fields):
        try:
            body = response.json()
        except Exception:
            assert False, "Тело не JSON"
        for f in fields:
            assert f in body, f"Поле {f} отсутствует в ответе"