from django.db import models
from accounts.models import User
    
class Question(models.Model):
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.content

# class User(models.Model):
#     username = models.TextField()
#     email = models.TextField()
#     password = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username
       
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='answer_images/')

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    
class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='letter_images/')

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    