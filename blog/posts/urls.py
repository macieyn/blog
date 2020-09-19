from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('tag/<str:slug>/', views.tag_detail, name='tag_detail'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
]