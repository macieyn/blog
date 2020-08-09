from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from . import views
from . import models

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

    def test_page_displays_posts(self):
        post = models.Post.objects.create(title='AbCdEf', content='GhIjKl')
        request = HttpRequest()
        response = views.home(request)
        html = response.content.decode('utf8')
        self.assertIn('AbCdEf', html)
        self.assertIn('GhIjKl', html)


class PostTests(TestCase):

    def test_post_created(self):
        models.Post.objects.create(title='AbCdEf', content='GhIjKl')
        post = models.Post.objects.first()
        self.assertEqual(post.title, 'AbCdEf')
        self.assertEqual(post.content, 'GhIjKl')
