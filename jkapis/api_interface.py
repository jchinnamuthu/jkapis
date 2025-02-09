import requests

class APIInterface:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers, params=params)
        return response.json()

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)
        return response.json()
