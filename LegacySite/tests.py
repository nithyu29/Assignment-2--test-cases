from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from LegacySite.models import Card

# Create your tests here.


class MyTest(TestCase):
    # Django's test run with an empty database. We can populate it with
    # data by using a fixture. You can create the fixture by running:
    #    mkdir LegacySite/fixtures
    #    python manage.py dumpdata LegacySite > LegacySite/fixtures/testdata.json
    # You can read more about fixtures here:
    #    https://docs.djangoproject.com/en/4.0/topics/testing/tools/#fixture-loading
    fixtures = ["testdata.json"]

    # Assuming that your database had at least one Card in it, this
    # test should pass.
    def test_get_card(self):
        allcards = Card.objects.all()
        self.assertNotEqual(len(allcards), 0)


class XssTest(TestCase):
    fixtures = ['testdata.json']

    def test_xss_attack(self):
        # Check that XSS attack is not possible anymore
        response = self.client.get(reverse('giftcard-detail', args=[1]))
        self.assertNotContains(response, '<script>alert("hello")</script>')


class XsrfTest(TestCase):
    fixtures = ['testdata.json']

    def test_xsrf_attack(self):
        # Check that XSRF attack is not possible anymore
        response = self.client.post(
            reverse('giftcard-update', args=[1]), {'amount': 100})
        self.assertContains(response, 'CSRF verification failed')

        from django.test import TestCase


class SqlInjectionTest(TestCase):
    fixtures = ['testdata.json']

    def test_sql_injection_attack(self):
        # Check that SQL injection attack is not possible anymore
        response = self.client.post(reverse('giftcard-upload'), {
                                    'file': open('sqli.gftcrd')})
        admin_password = User.objects.get(username='admin').password
        self.assertNotContains(response, admin_password)

        import subprocess


class CommandInjectionTest(TestCase):
    fixtures = ['testdata.json']

    def test_command_injection_attack(self):
        # Check that command injection attack is not possible anymore
        url = "http://localhost:8000/foo/2"
        response = self.client.post(url, {'var1': 'echo', 'var2': 'hello'})
        self.assertNotIn('hello', response.content.decode('utf-8'))

        # Check that the command was not executed on the server
        # cmd_output = subprocess.run(['cat', '/tmp/hello.txt'], stdout=subprocess.PIPE)
        # self.assertNotIn(b'hello', cmd_output.stdout)

# from django.test import TestCase, Client
# from django.urls import reverse
# from LegacySite.models import GiftCard

# class MyTest(TestCase):
#     def test_get_card(self):
#         giftcard = GiftCard.objects.create(amount=100)
#         allcards = GiftCard.objects.all()
#         self.assertNotEqual(len(allcards), 0)

# class XssTest(TestCase):
#     def test_xss_attack(self):
#         client = Client()
#         response = client.get(reverse('giftcard_detail', args=[1]))
#         self.assertNotIn('<script>', response.content.decode())

# class XsrfTest(TestCase):
#     def test_xsrf_attack(self):
#         client = Client(enforce_csrf_checks=True)
#         response = client.post(reverse('giftcard_update', args=[1]), {'amount': 100})
#         self.assertEqual(response.status_code, 403)

# class SqlInjectionTest(TestCase):
#     def test_sql_injection_attack(self):
#         client = Client()
#         response = client.post(reverse('giftcard_upload'), {
#             'amount': "100'; DROP TABLE LegacySite_giftcard; --"
#         })
#         self.assertEqual(GiftCard.objects.count(), 0)
