from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from slack.models import ChatMessage, Comments
from slack.forms import PostChatMessage, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import logging
# Create your views here.

def BaseHtmlSend(request):
    return render(request, 'Base.html', {'users':users}) 

def SingUpAccount(request):
    if request.method == "POST":
        username1 = request.POST['username']
        username2 = request.POST['username']
        nonhashpassword = request.POST['password']
        password1 = make_password(nonhashpassword)
        if username1 is None:
            try:
                User.objects.get(username=username1)
                return render(request, 'SignUp.html', {'error':'This username is already in use'})
            except:
                User.objects.create(username=username1, nickname=username2, password=password1)
                return render(request, 'Signup.html', {'success':'Account created successfully'})
        else:
            return render(request, 'SignUp.html', {})
    return render(request, 'SignUp.html', {})


def Login(request):
    if request.method == "POST":
        LoginUsername = request.POST['username']
        LoginPassword = request.POST['password']
        LoginUserInformation = authenticate(username=LoginUsername, password=LoginPassword)
        if LoginUserInformation is not None:
            login(request, LoginUserInformation)
            return redirect('chat')
        else:
            return render(request, 'Login.html', {})
    return render(request, 'Login.html', {})

@login_required
def SendChatMessage(request):
    form = PostChatMessage()
    if request.method == 'POST':
       form = PostChatMessage(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('chat')
    else:
           return render(request, 'ChatSend.html', {'error': 'Please type message'})
    return render(request, 'ChatSend.html', {'form':form})

@login_required
def ChatModel(request):
    object = ChatMessage.objects.order_by('created_date')
    return render(request, 'Chat.html', {'object':object})

def UserDetail(request, pk):
    detail = get_object_or_404(ChatMessage, pk=pk)
    return render(request, 'UserDetail.html', {'user_de':detail})  

def Logout(request):
    logout(request)
    return redirect('chat')

def DeleteView(request,pk):
    try:
        article = ChatMessage.objects.get(pk=pk)
        article.delete()
        return redirect('chat')
    except ChatMessage.DoesNotExist:
        raise Http404
    
def Good(request,pk):
    post = ChatMessage.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('chat')

class ChangeYourAccount(UpdateView):
    model = User
    fields = ('nickname', 'image', 'email')
    template_name = 'base.html'
    success_url = reverse_lazy('chat')

def CommentsSend(request, object_pk):
    detail = get_object_or_404(ChatMessage, pk=object_pk)
    return render(request, 'Comments.html', {'detail':detail}) 

def ChatComment(request, object_pk):
    post = get_object_or_404(ChatMessage, pk=object_pk)
    if request.method == 'POST':
        userform = CommentForm(request.POST)
        comment = userform.save(commit=False)
        comment.chatmessage = post
        userform.save()   
        return redirect('comment', object_pk=post.pk)
    else:
       return redirect('comment', post.pk)
    return redirect('comment') 