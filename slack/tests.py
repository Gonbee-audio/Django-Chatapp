from django.test import TestCase
from django.utils import timezone

import datetime

from accounts.models import User
from slack.models import ChatMessage, Comments, SecredMessage 


class TestSlack(TestCase):

    """Model
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images',blank=True, null=True)
    icon =models.CharField(max_length=1000)
    good = models.IntegerField(null=True, blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    """
    
    def test_chatmessage(self):

        saved_messages = ChatMessage.objects.all()
        self.assertFalse(saved_messages.count(), 0)

        testchat = ChatMessage.objects.create(
            username = "hogehgoe",
            nickname = "hogehgoe",
            text = "test",
            image = "test.png",
            thumbnail = "test.png",
            icon = "test",
            good = 0,
            created_date = datetime.datetime(2020, 11, 12, 9, 55, 28)
        )
        testMessage = testchat.text
        self.assertTrue("test", testMessage)
    

    """Model
    class Comments(models.Model):
    chatmessage = models.ForeignKey(ChatMessage, on_delete=models.CASCADE, related_name='items')
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000)
    icon =models.CharField(max_length=1000)
    
    def __str__(self):
        return self.text
    """
  
    def test_comments(self):

        
        chat = ChatMessage.objects.create(
            username = "hoge",
            nickname = "hoge",
            text = "tes",
            image = "test.png",
            thumbnail = "test.png",
            icon = "test",
            good = 0,
            created_date = datetime.datetime(2020, 11, 12, 9, 55, 28)
        )
        
        saved_comment_of_chat = Comments.objects.all()
        self.assertFalse(saved_comment_of_chat.count(), 0)


        comment_of_chat = Comments.objects.create(
                chatmessage = ChatMessage.objects.get(username="hoge", nickname="hoge"),
                username = "hoge",
                nickname = "hoge",
                text = "text",
                icon = "text",  
        )

        testComment = comment_of_chat.text
        self.assertTrue("test", testComment)


    def test_secred_essage(self):

        """
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usersend')
        username = models.CharField(max_length=30)
        yourname = models.CharField(max_length=30)
        nickname = models.CharField(max_length=30, null=True)
        text = models.CharField(max_length=1000)
        image = models.ImageField(upload_to='images',blank=True, null=True)
        icon =models.CharField(max_length=1000)
        created_date = models.DateTimeField(default=timezone.now)
        """
        User.objects.create(username="test", password="test")

        saved_secred_message = SecredMessage.objects.all()
        self.assertFalse(saved_secred_message.count(), 0)

        secred_message = SecredMessage.objects.create(
        user = User.objects.get(username="test", password="test"),
        username = "test",
        yourname = "test",
        nickname = "test",
        text = "test",
        image = "test.img",
        icon = "test",
        created_date = datetime.datetime(2020, 11, 12, 9, 55, 28)
        )

        text = secred_message.text
        self.assertTrue("test", text)




