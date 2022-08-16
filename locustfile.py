from locust import HttpUser, task, between

from dotenv import load_dotenv

from os import getenv
from utils import Logger

load_dotenv()

DEFAULT_API_ENDPOINT = getenv('API_ENDPOINT', '')

file_logger = Logger.LogToFile(filename = getenv('LOG_FILE'), mode=getenv('LOG_MODE'))


# Uncomment @task to add the task for load testing


class APIUser(HttpUser):
    # wait_time = between(1, 7)
    def on_start(self):
        pass  # add code to run during ramp up

    def on_stop(self):
        pass  # add code to run during ramp down

    @task
    def api_get_endpoint_test(self):
        _HEADERS = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br", 
            "Connection": "keep-alive"
        }
        self.client.get(DEFAULT_API_ENDPOINT, headers = _HEADERS)

    # @task
    def api_post_endpoint_test(self):
        _JSON = {}
        _HEADERS = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br", 
            "Connection": "keep-alive"
        }
        self.client.post(DEFAULT_API_ENDPOINT, headers = _HEADERS, json = _JSON)

# locust -f locustfile.py --host <host url> --headless -u 1 -r 1