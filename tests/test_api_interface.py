import unittest
from unittest.mock import patch
from jkapis import APIInterface

class TestAPIInterface(unittest.TestCase):

    @patch('requests.get')
    def test_get(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        api = APIInterface(base_url="https://api.example.com", token="test_token")
        response = api.get("test_endpoint")
        self.assertEqual(response, {'key': 'value'})
        mock_get.assert_called_once_with("https://api.example.com/test_endpoint", headers=api.headers, params=None)

    @patch('requests.post')
    def test_post(self, mock_post):
        mock_post.return_value.json.return_value = {'key': 'value'}
        api = APIInterface(base_url="https://api.example.com", token="test_token")
        response = api.post("test_endpoint", data={"key": "value"})
        self.assertEqual(response, {'key': 'value'})
        mock_post.assert_called_once_with("https://api.example.com/test_endpoint", headers=api.headers, json={"key": "value"})

if __name__ == '__main__':
    unittest.main()
