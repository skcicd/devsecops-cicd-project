import unittest
from src.app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, DevSecOps!', response.data)

if __name__ == '__main__':
    unittest.main()
