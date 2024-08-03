from django.db import models

class Funeral(models.Model):
    name = models.CharField(max_length=200, blank=False)
    region = models.CharField(max_length=100, unique=False, blank=False)
    address = models.CharField(max_length=300, unique=True, blank=False)
    phone = models.CharField(max_length=20, unique=True, blank=False) # PhoneNumberField()라는 것도 있는데 일단 사용 안함
    image = models.ImageField(upload_to='funeral_images/', blank=True, null=True)
    website = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name