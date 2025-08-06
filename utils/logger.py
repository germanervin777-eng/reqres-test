import json
import datetime
import os
import allure

os.makedirs("logs", exist_ok=True)
logfile = f"logs/log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def _write(msg):
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

class Logger:
    @staticmethod
    def add_request(url, method, body=None):
        text = f"REQUEST -> {method} {url}"
        if body:
            try:
                pretty = json.dumps(body, ensure_ascii=False)
            except:
                pretty = str(body)
            text += f"\nBody: {pretty}"
        _write(text)
        try:
            allure.attach(text, name="request", attachment_type=allure.attachment_type.TEXT)
        except:
            pass

    @staticmethod
    def add_response(response):
        try:
            body = response.text
        except:
            body = "<no body>"
        text = f"RESPONSE <- {response.request.method} {response.url}\nStatus: {response.status_code}\nBody: {body}"
        _write(text)
        try:
            allure.attach(text, name="response", attachment_type=allure.attachment_type.TEXT)
        except:
            pass