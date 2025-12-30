from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Account
from .forms import SignupForm, LoginForm, PostForm
import pdb


def home(request):
    return render(request, 'home.html')


def signup_view(request):
    form = SignupForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user_obj = Account.objects.filter(email=email).first()

            if user_obj and user_obj.check_password(password):
                login(request, user_obj)
                return redirect('post_list')

            form.add_error(None, "Invalid email or password")

    return render(request, 'login.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login_view')
def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    return render(request, 'create_post.html', {'form': form})


def user_post_list(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'post_list.html', {'posts': posts})

def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('post_list')

    return render(request, 'update.html', {'form': form})