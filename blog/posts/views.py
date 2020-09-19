from django.shortcuts import render, get_object_or_404

from . import models

# Create your views here.

def home(request):
    posts = models.Post.objects.all().order_by('-created_at')
    featured = models.Post.get_featured(3)
    tags = models.Tag.objects.all()
    context={
        'title': "Witaj w Notatniku Juniora",
        'subtitle': "O czym chcesz poczytać?",
        'tags': tags,
        'posts': posts,
        'featured': featured,
    }
    return render(request, 'home_page.html', context)

def tag_detail(request, slug):
    context = {
        'tag': get_object_or_404(models.Tag, slug=slug)
    }
    return render(request, 'base.html', context)

def post_detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    if request.user != post.author:
        post.views += 1
        post.save()
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)