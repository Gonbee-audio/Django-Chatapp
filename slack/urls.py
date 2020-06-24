from django.urls import path
from slack.views import SingUpAccount, Login, ChatModel, SendChatMessage, Logout, DeleteView, Good, LoginUser

urlpatterns = [
    path('SignUp/', SingUpAccount, name="signup"),
    path('Login/', Login, name="login"),
    path('Chat/', ChatModel, name="chat"),
    path('ChatSend/', SendChatMessage, name="sendchatmessage"),
    path('Logout/', Logout, name="logout"),
    path('Chat/<int:pk>/Delete', DeleteView, name="delete"),
    path('Chat/<int:pk>/Good', Good, name="good"),
    path('Loginuser/', LoginUser, name="loginuser")
]