from django.shortcuts import render
from django.views import  View
# Create your views here.       'base.html'
from django.http import HttpResponse
from .models import Post,User


def home(request):
    context = { 'text' : 'Helllo, world'}
    print(context)
    return render(request, 'index.html', context)


class Profile(View):
    """User Profile Page */user/<username>"""
    def get(self, request, username):
        user = User.objects.get (username = username)
        posts = Post.objects.filter (user = user)
        context = {
            'posts' : posts,
            'user' : user,
        }
        return render(request, 'profile.html', context)