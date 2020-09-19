from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.utils import timezone

from . import views
from . import models

User = get_user_model()

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
        post = models.Post.objects.create(title='AbCdEf', content='GhIjKl', slug='abcd')
        request = HttpRequest()
        response = views.home(request)
        html = response.content.decode('utf8')
        self.assertIn('AbCdEf', html)
        self.assertIn('GhIjKl', html)


class PostTests(TestCase):
    def setUp(self):
        User.objects.create(username='u', email='a@aa.com', password='pass')
        return super().setUp()

    def test_post_created(self):
        user = User.objects.first()
        models.Post.objects.create(title='AbCdEf', content='GhIjKl', author=user)
        post = models.Post.objects.first()
        self.assertEqual(post.title, 'AbCdEf')
        self.assertEqual(post.content, 'GhIjKl')
        self.assertEqual(post.author, user)

class PostOperationsTests(TestCase):
    # TODO: mock time of post creation 
    
    def setUp(self):
        user = User.objects.create(username='u', email='a@aa.com', password='pass')
        models.Post.objects.create(
            title='AbCdEf', 
            content='GhIjKl', 
            author=user)
        return super().setUp()
    
    def test_post_modified(self):
        post = models.Post.objects.first()
        post.content = 'MnOpQrS'
        post.save()
        self.assertEqual(post.content, 'MnOpQrS')
        self.assertNotEqual(post.modified_at, post.created_at)
