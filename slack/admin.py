from django.contrib import admin
from .models import ChatMessage, Comments, SecredMessage

admin.site.register(ChatMessage)
admin.site.register(Comments)
admin.site.register(SecredMessage)
# Register your models here.
