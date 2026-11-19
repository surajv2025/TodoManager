from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    owner=models.ForeignKey('auth.User', on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.task}" 
    
class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"    