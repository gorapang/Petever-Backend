from django.db import models
from accounts.models import User
#from django.conf import settings  # 수정된 부분

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='memorials/gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"GalleryImage {self.id} - {self.image.url}"


class Memorial(models.Model):
    user = models.ForeignKey(User, related_name='memorials', on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=200)  # 반려동물 이름
    birth_date = models.DateField()  # 탄생일
    death_date = models.DateField()  # 사망일
    memorial_name = models.CharField(max_length=200)  # 추모 공간 이름
    memorial_tagline = models.CharField(max_length=255)  # 추모 공간 대표 문구
    main_image = models.ImageField(upload_to='memorials/main_images/')  # 추모 공간 대표 이미지
    message = models.TextField()  # 전하고 싶은 말
    gallery_images = models.ManyToManyField(GalleryImage, related_name='memorials')  # 남기고 싶은 사진
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memorial_name


class Footprint(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=100)
    memorial = models.ForeignKey(Memorial, related_name='footprints', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.content[:20]}"
