from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from colorfield.fields import ColorField
from django.shortcuts import reverse
from ckeditor.fields import RichTextField


# Create your models here.

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=30)
    color = ColorField(default='#FF0000')
    text_color = models.CharField(max_length=7, default='#000000')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.text_color = self.contrast_color()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def contrast_color(self):
        color = self.color[1:]
        r = int(color[0:2], base=16)
        g = int(color[2:4], base=16)
        b = int(color[4:6], base=16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return '#000000' if luminance > 0.8 else '#FFFFFF'


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField(config_name='default')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    featured = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return f'Post: {self.title}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.modified_at = timezone.now()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def is_modified(self):
        return self.modified_at.date() > self.published_at.date()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_tags(self):
        return Tag.objects.filter(post=self)
    