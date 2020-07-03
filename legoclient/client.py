from legoclient.request import ApiRequest


class Client:

    DEFAULT_BASE_URL='http://localhost:5000/api/v1'

    def __init__(self, base_url=DEFAULT_BASE_URL):
        self.base_url = base_url
        self.headers = None
        self.token = None
        self.request = ApiRequest()

    def login(self, username, password):
        url = f'{self.base_url}/auth/login'
        data = {
            'username': username,
            'password': password
        }

        self.build_headers()

        output = self.request.post(url, data, self.headers)

        if output['result']:
            self.token = output['data']
            self.build_headers()

        return output

    def build_headers(self):
        if self.token:
            self.headers = {
                'Content-Type': 'application/json',
                'X-API-KEY': self.token
            }
        else:
            self.headers = {
                'Content-Type': 'application/json'
            }

    def products(self):
        url = f'{self.base_url}/products'

        return self.request.get(url, headers=self.headers)

    def product(self, product_id):
        endpoint = f'{self.base_url}/products/{product_id}'

        return self.request.get(endpoint, headers=self.headers)

    def create(self, data):
        url = f'{self.base_url}/products/'

        return self.request.post(url, data, self.headers)

    def update(self, product_id, data):
        url = f'{self.base_url}/products/{product_id}'

        return self.request.put(url, data, self.headers)

    def delete(self, product_id):
        url = f'{self.base_url}/products/{product_id}'

        return self.request.delete(url, self.headers)
