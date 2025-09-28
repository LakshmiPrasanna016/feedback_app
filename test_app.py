import unittest
from app import app

class FeedbackTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_feedback_post(self):
        response = self.client.post('/feedback', json={'name': 'Alice', 'message': 'Great app!'})
        self.assertEqual(response.status_code, 200)

    def test_feedback_get(self):
        response = self.client.get('/feedback')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

