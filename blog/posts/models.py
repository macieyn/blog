from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone

# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.modified_at = timezone.now()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)