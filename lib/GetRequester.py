import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        return None

    def load_json(self):
        body = self.get_response_body()
        if body:
            return json.loads(body.decode("utf-8"))  # Decoding bytes to string and loading JSON
        return None
