import unittest
from app import app
import pytest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @pytest.mark.unit
    def test_hello_world(self):
        """Test that the root endpoint returns 'Hello, World!'"""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
