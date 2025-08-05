from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False, blank=False)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mark_for_deletion = models.BooleanField(default=False)

class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mark_for_deletion = models.BooleanField(default=False)