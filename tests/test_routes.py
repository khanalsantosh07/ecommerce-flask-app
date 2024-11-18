import unittest
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app import app

class TestRoutes(unittest.TestCase):
    """Test Flask application routes."""

    def setUp(self):
        self.app = app.test_client()

    def test_invalid_method(self):
        """Test the / route with an invalid HTTP method (POST instead of GET)."""
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
