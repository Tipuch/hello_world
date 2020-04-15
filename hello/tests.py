from datetime import date

from django.test import TestCase

from hello.models import Person


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,
                         b'<html><body>Hello World!</body></html>')


class TestPersonModel(TestCase):
    def setUp(self):
        Person.objects.create(name="Jeremy",
                              date_of_birth=date(2016, 3, 17),
                              gender=Person.MALE)

    def test_person_model(self):
        jeremy = Person.objects.get(name="Jeremy")
        self.assertEqual(str(jeremy), "Jeremy born 2016-03-17")
