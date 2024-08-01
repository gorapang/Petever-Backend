from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when created

    def __str__(self):
        return self.username
