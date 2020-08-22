from django.shortcuts import render, get_object_or_404

from . import models

# Create your views here.

def home(request):
    posts = models.Post.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'posts/post_feed.html', context)

def tag_detail(request, slug):
    context = {
        'tag': get_object_or_404(models.Tag, slug=slug)
    }
    return render(request, 'base.html', context)

def post_detail(request, slug):
    context = {
        'post': get_object_or_404(models.Post, slug=slug)
    }
    return render(request, 'base.html', context)