import unittest
from app import app

class TestSumEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sum_endpoint_valid_numbers(self):
        # Test with positive numbers
        response = self.app.get('/api/sum?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8.0)
        self.assertEqual(response.json['status'], 'success')

        # Test with decimal numbers
        response = self.app.get('/api/sum?num1=2.5&num2=3.7')
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json['result'], 6.2)
        self.assertEqual(response.json['status'], 'success')

    def test_sum_endpoint_missing_parameters(self):
        # Test with missing parameters (should default to 0)
        response = self.app.get('/api/sum')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 0.0)
        self.assertEqual(response.json['status'], 'success')

    def test_sum_endpoint_invalid_input(self):
        # Test with non-numeric input
        response = self.app.get('/api/sum?num1=abc&num2=3')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['status'], 'error')

        response = self.app.get('/api/sum?num1=5&num2=xyz')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['status'], 'error')

if __name__ == '__main__':
    unittest.main()
