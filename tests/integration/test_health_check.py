import unittest
import requests
from app import app
import pytest

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.base_url = 'http://localhost:6001'

    @pytest.mark.integration
    def test_health_check(self):
        """Test that the application is alive and responding"""
        # Test using the test client (faster, no need to run the server)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')
        
        # Test using actual HTTP request (comment out if you don't want to test against a running server)
        try:
            response = requests.get(f'{self.base_url}/', timeout=5)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.text, 'Hello, World!')
        except requests.exceptions.RequestException as e:
            self.skipTest(f"Could not connect to {self.base_url}: {e}")

if __name__ == '__main__':
    unittest.main()
