from django.shortcuts import render

# Create your views here.
# posts/views.py

from django.shortcuts import render
from .models import Post

def home(request):

    posts = Post.objects.all()

    return render(request, 'home.html', {
        'posts': posts
    })