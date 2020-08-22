from django import forms
from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)