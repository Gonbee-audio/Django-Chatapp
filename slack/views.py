from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from accounts.models import User
from slack.models import ChatMessage, Comments, SecredMessage
from slack.forms import PostChatMessage, CommentForm, UpdataForm, SecredSendForm
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
        try:
            User.objects.get(username=username1)
            return render(request, 'SignUp.html', {'error':'This username is already in use'})
        except:
            User.objects.create(username=username1, nickname=username2, password=password1)
            # return render(request, 'Login.html', {'success':'Successfully created account'})
            return redirect('chat')
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
    if request.method == 'POST':
       form = PostChatMessage(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('chat')
    else:
           return render(request, 'Chat.html', {'error': 'Please type message'})
    return redirect('chat')

@login_required
def ChatModel(request):
    object = ChatMessage.objects.order_by('created_date')
    return render(request, 'Chat.html', {'object':object})

def UserDetail(request, pk, other_pk):
    detail = get_object_or_404(User, pk=pk)
    yourid = User.objects.all().filter(
        Q(pk=pk) | Q(pk=other_pk)
    )
    return render(request, 'UserDetail.html', {'user_de':detail, 'users':yourid})  

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

def ChangeYourAccount(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(User, pk=pk)
        form = UpdataForm(request.POST, request.FILES, instance=post)
        form.save() 
        username1 = request.POST['username']
        nickname1 = request.POST['nickname']
        image1 = post.image.url
        logging.debug(image1)
        c = ChatMessage.objects.filter(username=username1)
        for new in c:
            new.nickname = nickname1
            new.icon = image1
            new.save()
            co = Comments.objects.filter(username=username1)
            for new in co:
                new.nickname = nickname1
                new.icon = image1
                new.save()
                ch = Comments.objects.filter(username=username1)
                for new in ch:
                    new.nickname = nickname1
                    new.icon = image1
                    new.save()
        return redirect('chat')
    else:
        return redirect('chat')

def CommentsSend(request, object_pk):
    detail = get_object_or_404(ChatMessage, pk=object_pk)
    return render(request, 'Comments.html', {'detail':detail}) 

def ChatComment(request, object_pk):
    post = get_object_or_404(ChatMessage, pk=object_pk)
    if request.method == 'POST':
        userform = CommentForm(request.POST, request.FILES)
        comment = userform.save(commit=False)
        comment.chatmessage = post
        userform.save()   
        return redirect('comment', object_pk=post.pk)
    else:
       return redirect('comment', post.pk)
    return redirect('comment') 

def SecredMessageCreate(request, pk, other_pk):
    if request.method == 'POST':
        users = get_object_or_404(User, pk=pk)
        yours = get_object_or_404(User, pk=other_pk)
        userform = SecredSendForm(request.POST, request.FILES)
        if userform.is_valid():
            comment = userform.save(commit=False)
            comment.user = users
            userform.save()   
        return redirect('userdetail',pk=pk, other_pk=other_pk)
    else:
       return redirect('userdetail')
    return redirect('userdetail') 