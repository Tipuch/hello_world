from django.test import TestCase


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'<html><body>Hello World!</body></html>')
