from django import forms
from .models import ChatMessage

class PostChatMessage(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('username','text','image', 'good')
    