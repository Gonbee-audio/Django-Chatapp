from django import forms
from .models import ChatMessage, Comments, SecredMessage
from accounts.models import User
from django.core.exceptions import ValidationError
import logging


class PostChatMessage(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('username','nickname', 'text','image', 'icon')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('username', 'text','icon')

class UpdataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'image')

class RemakeSendForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('nickname', 'icon')

class SecredSendForm(forms.ModelForm):
    class Meta:
        model = SecredMessage
        fields = ('yourname', 'username', 'nickname','image', 'text', 'icon')