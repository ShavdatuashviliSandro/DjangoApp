from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_answered = models.BooleanField(default=False)
    mark_for_deletion = models.BooleanField(default=False)
