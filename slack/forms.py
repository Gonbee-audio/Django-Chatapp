from django import forms
from .models import ChatMessage, Comments

class PostChatMessage(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('username','text','image', 'icon')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('username', 'text','icon')