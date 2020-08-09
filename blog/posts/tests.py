from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from . import views

# Create your tests here.

class PostPageTests(TestCase):

    def test_resolve(self):
        response = resolve('/')
        self.assertEqual(views.home, response.func)

    def test_returns_html(self):
        request = HttpRequest()
        response = views.home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertTrue(html.endswith('</html>'))
