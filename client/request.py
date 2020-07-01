import requests
import json


class ApiRequest:
    @staticmethod
    def get(url, headers):
        response = requests.get(url, headers=headers)

        return json.loads(response.content.decode('utf-8'))

    @staticmethod
    def post(url, data, headers):
        response = requests.post(url, json=data, headers=headers)

        return json.loads(response.content.decode('utf-8'))

    @staticmethod
    def put(url, data, headers):
        response = requests.put(url, json=data, headers=headers)

        return response.content.decode('utf-8')

    @staticmethod
    def delete(url, headers):
        response = requests.delete(url, headers=headers)

        return json.loads(response.content.decode('utf-8'))
