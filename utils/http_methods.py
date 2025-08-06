import requests

class HttpMethods:
    headers = {
        "Content-type": "application/json",
        "x-api-key": "reqres-free-v1",
    }

    @staticmethod
    def get(url, params=None):
        if params:
            return requests.get(url, headers=HttpMethods.headers, params=params)
        return requests.get(url, headers=HttpMethods.headers)

    @staticmethod
    def post(url, json_body=None):
        return requests.post(url, json=json_body, headers=HttpMethods.headers)

    @staticmethod
    def put(url, json_body=None):
        return requests.put(url, json=json_body, headers=HttpMethods.headers)

    @staticmethod
    def delete(url):
        return requests.delete(url, headers=HttpMethods.headers)