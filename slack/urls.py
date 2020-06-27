from django.urls import path
from slack.views import SingUpAccount, Login, ChatModel, SendChatMessage, Logout, DeleteView, Good, ChangeYourAccount, CommentsSend, ChatComment

urlpatterns = [
    path('SignUp/', SingUpAccount, name="signup"),
    path('Login/', Login, name="login"),
    path('Chat/', ChatModel, name="chat"),
    path('ChatSend/', SendChatMessage, name="sendchatmessage"),
    path('Logout/', Logout, name="logout"),
    path('Chat/<int:pk>/Delete', DeleteView, name="delete"),
    path('Chat/<int:pk>/Good', Good, name="good"),
    path('settings/<int:pk>/account/', ChangeYourAccount.as_view(), name="change"),
    path('Comments/<int:pk>', CommentsSend, name="comment"),
    path('Comments/<int:object_pk>/ChatComment', ChatComment, name="chatcomment")
]