from django.urls import path
from .views import fbv_api_list, fbv_post_detail

urlpatterns = [
    path('posts/', fbv_api_list),
    path('posts/<int:pk>/', fbv_post_detail),
]