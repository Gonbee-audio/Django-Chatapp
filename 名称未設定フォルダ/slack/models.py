from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class ChatMessage(models.Model):
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images',blank=True, null=True)
    icon =models.ImageField(upload_to='images',blank=True, null=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    favorite = models.IntegerField(null=True, blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username

class Comments(models.Model):
    chatmessage = models.ForeignKey(ChatMessage, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    icon =models.ImageField(upload_to='images',blank=True, null=True)
    chatlog = models.IntegerField(null=True, blank=False, default=0)
    
    def __str__(self):
        return str(self.chatmessage_id)

