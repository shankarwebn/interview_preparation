
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('post_list/',views.post_list, name='post_list'),
    path('logout_view/',views.logout_view, name='logout_view'),
    path('login_view/',views.login_view, name='login_view'),
    path('create_post/',views.create_post, name='create_post'),
    path('user_post_list/',views.user_post_list, name='user_post_list')   
]
    