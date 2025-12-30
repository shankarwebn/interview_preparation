from django  import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Account,Post

class SignupForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username','email','password1','password2','address','phone']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' 