from legoclient.request import ApiRequest


class Client:

    DEFAULT_BASE_URL='http://localhost:1337'

    def __init__(self, base_url=DEFAULT_BASE_URL):
        self.base_url = base_url
        self.headers = None
        self.jwt = None
        self.name = None
        self.username = None
        self.email = None
        self.request = ApiRequest()

    def login(self, email, password):
        url = f'{self.base_url}/auth/local'
        data = {
            'identifier': email,
            'password': password
        }

        self.build_headers()

        response = self.request.post(url, data, self.headers)

        if response['jwt']:
            self.jwt = response['jwt']
            self.name = response['user']['name']
            self.username = response['user']['username']
            self.email = response['user']['email']
            self.build_headers()

        return self

    def build_headers(self):
        if self.jwt:
            self.headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.jwt}'
            }
        else:
            self.headers = {
                'Content-Type': 'application/json'
            }

    def product_list(self):
        url = f'{self.base_url}/products/'

        return self.request.get(url, headers=self.headers)

    def product_get(self, product_id):
        endpoint = f'{self.base_url}/products/{product_id}'

        return self.request.get(endpoint, headers=self.headers)

    def product_create(self, data):
        url = f'{self.base_url}/products/'

        return self.request.post(url, data, self.headers)

    def product_update(self, product_id, data):
        url = f'{self.base_url}/products/{product_id}'

        return self.request.put(url, data, self.headers)

    def product_delete(self, product_id):
        url = f'{self.base_url}/products/{product_id}'

        return self.request.delete(url, self.headers)

    def price_check_list(self):
        url = f'{self.base_url}/price-checks/'

        return self.request.get(url, headers=self.headers)

    def price_check_create(self, data):
        url = f'{self.base_url}/price-checks/'

        return self.request.post(url, data, self.headers)
