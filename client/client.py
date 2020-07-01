import json
import requests


class Client():
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers
        self.token = None

    def login(self, username, password):
        endpoint = f'{self.base_url}/auth/login'
        payload = json.dumps({
            "username": username,
            "password": password
        })

        headers = self.build_headers()

        response = requests.post(endpoint, data=payload, headers=headers)

        if response.status_code == 200:
            output = json.loads(response.content.decode('utf-8'))
            self.token = output['data']
            return True
        else:
            return False

    def build_headers(self):
        if self.token:
            headers = {
                'Content-Type': 'application/json',
                'X-API-KEY': self.token
            }
        else:
            headers = {
                'Content-Type': 'application/json'
            }

        return headers

    def products(self):
        endpoint = f'{self.base_url}/products'
        headers = self.build_headers()

        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def product(self, product_id):
        endpoint = f'{self.base_url}/products/{product_id}'
        headers = self.build_headers()

        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def create(self, data):
        endpoint = f'{self.base_url}/products/'
        headers = self.build_headers()
        payload = json.dumps(data)

        response = requests.post(endpoint, data=payload, headers=headers)

        return json.loads(response.content.decode('utf-8'))

    def update(self, product_id, data):
        endpoint = f'{self.base_url}/products/{product_id}'
        headers = self.build_headers()
        payload = json.dumps(data)

        response = requests.put(endpoint, data=payload, headers=headers)

        return json.loads(response.content.decode('utf-8'))

    def delete(self, product_id):
        endpoint = f'{self.base_url}/products/{product_id}'
        headers = self.build_headers()

        response = requests.delete(endpoint, headers=headers)

        return json.loads(response.content.decode('utf-8'))
