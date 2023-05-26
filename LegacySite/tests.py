import os
from django.test import TestCase
from django.urls import reverse
from LegacySite.models import Card

# Create your tests here.

class MyTest(TestCase):
    fixtures = ["testdata.json"]

    def test_get_card(self):
        allcards = Card.objects.all()
        self.assertNotEqual(len(allcards), 0)

    def test_sql_injection(self):
        malicious_input = "' OR 1=1; --"
        response = self.client.get(reverse("search"), {"q": malicious_input})
        self.assertNotContains(response, "SELECT * FROM users;")

    def test_upload_file_sql_injection(self):
        payload = "'; DROP TABLE users;"

        with open('sql_injection_payload.txt', 'w') as f:
            f.write(payload)

        with open('sql_injection_payload.txt', 'rb') as f:
            response = self.client.post(reverse('upload_file'), {'param': f})

        self.assertNotContains(response, 'Error')

        os.remove('sql_injection_payload.txt')

    def test_command_injection(self):
        payload = "foo"
        response = self.client.post(reverse('search'), {'search': payload})

        file_path = os.path.join(os.getcwd(), "foo")

        with open(file_path, 'w') as file:
            pass

        self.assertTrue(os.path.exists(file_path))


