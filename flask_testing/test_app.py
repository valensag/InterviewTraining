# test_app.py

import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_prime_number(self):
        response = self.app.post('/is_prime_number', json={'number': 7})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'number': 7, 'is_prime_number': True})

    def test_non_prime_number(self):
        response = self.app.post('/is_prime_number', json={'number': 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'number': 4, 'is_prime_number': False})

    def test_invalid_number(self):
        response = self.app.post('/is_prime_number', json={'number': 'not_a_number'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input, please enter an integer'})

if __name__ == '__main__':
    unittest.main()
