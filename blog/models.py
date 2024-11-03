from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # السماح بـ null
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
