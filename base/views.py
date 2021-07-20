from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group, User




from .models import *
from .forms import CreateUserForm
from .decorators import admin_only, allowed_users, unauthenticated_user
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            userino = form.cleaned_data
            User.objects.create_user(userino.get('username'), userino.get('email'), userino.get('password1'))
            messages.success(request, 'Account was created for '+ form.cleaned_data.get('username'))
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect.")
    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {}    
    return render(request, "base/main.html", context)

@login_required(login_url='login')
def bob(request ,username=None):
    bob = User.objects.get(name=username)

    posts = bob.post_set.all()
    posts_count = posts.count()

    context = {'bob': bob, 'posts':posts, 'posts_count':posts_count}

    return render(request, "base/bob_profile.html", context)

@login_required(login_url='login')
def profile(request):
    # user = Bob.objects.get()
    # context = {'user': user}

    return render(request, "base/profile.html")

@login_required(login_url='login')
def blog(request):

    bobs = Bob.objects.all()
    posts = Post.objects.all()
    context = {'bobs':bobs, 'posts': posts}

    return render(request, "base/blog.html", context)