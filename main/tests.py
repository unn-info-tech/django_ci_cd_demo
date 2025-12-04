from django.test import TestCase

class SimpleTest(TestCase):
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 40400)

    def test_homepage_content(self):
        response = self.client.get('/')
        self.assertContains(response, "Hello, Django!")
