from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):


    context = {}    
    return render(request, "base/main.html", context)


def bob(request, pk):
    bob = Bob.objects.get(id=pk)

    posts = bob.post_set.all()
    posts_count = posts.count()

    context = {'bob': bob, 'posts':posts, 'posts_count':posts_count}

    return render(request, "base/bob_profile.html", context)


def profile(request):
    # user = Bob.objects.get()
    # context = {'user': user}

    return render(request, "base/profile.html")


def blog(request):

    bobs = Bob.objects.all()
    posts = Post.objects.all()
    context = {'bobs':bobs, 'posts': posts}

    return render(request, "base/blog.html", context)