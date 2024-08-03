from django.db import models

class Memorial(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='memorials/main_images/')
    gallery_images = models.ManyToManyField('GalleryImage', related_name='memorials')
    message = models.TextField()
    birth_date = models.DateField()
    death_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='memorials/gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"GalleryImage {self.id} - {self.image.url}"


class Footprint(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=100)
    memorial = models.ForeignKey(Memorial, related_name='footprints', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.content[:20]}"
