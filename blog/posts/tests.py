from django.test import TestCase
from django.urls import resolve

from . import views

# Create your tests here.

class PostPageTests(TestCase):

    def test_resolve(self):
        response = resolve('/')
        self.assertEqual(views.posts, response.func)

    def test_return_http_re