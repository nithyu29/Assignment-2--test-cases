import os
import django

from django.test import TestCase
from .models import Card
from .models import Card, Product
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from LegacySite.models import Card

# Create your tests here.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GiftcardSite.settings')
django.setup()


class MyTest(TestCase):
    # Django's test run with an empty database. We can populate it with
    fixtures = ["testdata.json"]

    # Assuming that your database had at least one Card in it, this
    # test should pass.
    def test_get_card(self):
        allcards = Card.objects.all()
        self.assertNotEqual(len(allcards), 0)

    # def test_sql_injection(self):
    #     # This test assumes that your server accepts a GET request at the
    #     # URL '/search/' with a query parameter named 'q'.
    #     malicious_input = "' OR 1=1; --"
    #     response = self.client.get(reverse("search"), {"q": malicious_input})
    #     # Verify that the response does not contain any results that are not
    #     # related to the search term.
    #     self.assertNotContains(response, "SELECT * FROM users;")
# from django.test import TestCase
#
# class MyTest(TestCase):
    def test_upload_file_sql_injection(self):
        # Construct SQL injection payload
        payload = "'; DROP TABLE users;"

        # Open a file with the payload as its contents
        f = open('sql_injection_payload.txt', 'w')
        f.write(payload)
        f.close()

        # Upload the file to the server
        with open('sql_injection_payload.txt', 'rb') as f:
            response = self.client.post('/url/', {'param': f})

        # Verify that the response does not contain any sensitive data
        self.assertNotContains(response, 'Error')

        # Clean up the uploaded file
        os.remove('sql_injection_payload.txt')

    # def test_command_injection(self):
    #     # Construct command injection payload
    #     payload = "touch foo"
    #
    #     # Submit payload to form
    #     response = self.client.post('/url/', {'search': payload})
    #
    #     # Check if the file was created
    #     self.assertTrue(os.path.exists('foo'))

    def test_command_injection(self):
        # Inject command into form
        payload = "touch foo"
        response = self.client.post('/url/', {'search': payload})

        # Check if file was created
        file_path = os.path.join(os.getcwd(), "foo")
        self.assertTrue(os.path.exists(file_path))

# def test_upload_file_sql_injection(self):
#     # Construct SQL injection payload
#     payload = "'; DROP TABLE users;"
#
#     # Open a file with the payload as its contents
#     f = open('sql_injection_payload.txt', 'w')
#     f.write(payload)
#     f.close()
#
#     # Upload the file to the server using a parameterized query
#     response = self.client.post('/url/', {'param': (payload,)})
#
#     # Verify that the response does not contain any sensitive data
#     self.assertNotContains(response, 'Error')
#
#     # Clean up the uploaded file
#     os.remove('sql_injection_payload.txt')
