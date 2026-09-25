# realtimeproject/urls.py

from django.contrib import admin
from django.urls import path
from posts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]