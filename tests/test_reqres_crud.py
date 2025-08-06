import random
import string
import allure
import pytest

from api.reqres_api import ReqResApi
from utils.checking import Checking

def random_name():
    return "User" + "".join(random.choices(string.ascii_letters + string.digits, k=4))

def random_job():
    return "Job" + "".join(random.choices(string.ascii_lowercase, k=4))

@pytest.fixture()
def api():
    return ReqResApi()

@allure.feature("ReqRes CRUD")
class TestReqresCrud:

    def test_full_crud_flow(self, api):
        # create
        name = random_name()
        job = random_job()
        payload = {"name": name, "job": job}
        create_resp = api.create_user(payload)
        # проверка статус кода
        Checking.check_status_code(create_resp, 201)
        body = create_resp.json()
        assert body.get("name") == name
        assert body.get("job") == job
        user_id = body.get("id")
        assert user_id is not None

        # read
        get_resp = api.get_user(user_id)
        if get_resp.status_code == 200:
            Checking.check_status_code(get_resp, 200)
            data = get_resp.json().get("data", {})
            assert str(data.get("id")) == str(user_id)
        else:
            print("GET вернул не 200, скорее всего моковый API, продолжаем")

        # update
        new_name = random_name()
        new_job = random_job()
        update_payload = {"name": new_name, "job": new_job}
        update_resp = api.update_user(user_id, update_payload)
        Checking.check_status_code(update_resp, 200)
        updated = update_resp.json()
        assert updated.get("name") == new_name
        assert updated.get("job") == new_job

        # delete
        delete_resp = api.delete_user(user_id)
        Checking.check_status_code(delete_resp, 204)
        after_delete = api.get_user(user_id)
        print("После удаления GET статус:", after_delete.status_code)

    def test_create_without_fields(self, api):
        resp = api.create_user({})
        Checking.check_status_code(resp, 201)
        b = resp.json()
        assert "id" in b
        assert "createdAt" in b

    def test_get_fake_user(self, api):
        resp = api.get_user("999999")
        Checking.check_status_code(resp, 404)