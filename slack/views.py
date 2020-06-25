from django.shortcuts import render, redirect
from accounts.models import User
from slack.models import ChatMessage
from slack.forms import PostChatMessage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

def SingUpAccount(request):
    if request.method == "POST":
        username1 = request.POST['username']
        username2 = request.POST['username']
        password1 = request.POST['password']
        try:
            User.objects.get(username=username1)
            return render(request, 'SignUp.html', {'error':'This username is already in use'})
        except:
            User.objects.create(username=username1, nickname=username1, password=password1)
            return render(request, 'Signup.html', {'success':'Account created successfully'})
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
           form = PostChatMessage()
           return render(request, 'ChatSend.html', {'error': 'Please type message'})
    return render(request, 'ChatSend.html', {'form':form})

@login_required
def ChatModel(request):
    object = ChatMessage.objects.all()
    return render(request, 'Chat.html', {'object':object}) 

def Logout(request):
    logout(request)
    return redirect('login')

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

#def ChangeYourAccount(request,pk):
#    if request.method == 'POST':
#            User.objects.get(pk=pk)
#            form = PostChatMessage(request.POST, request.FILES)
#            if form.is_valid():
#                form.save()
#                return redirect('chat')
#        except:
#            return redirect('chat')
##        return redirect('chat')

class ChangeYourAccount(UpdateView):
    model = User
    fields = ('nickname', 'image', 'email')
    template_name = 'base.html'
    success_url = reverse_lazy('chat')