from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import signup, login, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('', include(router.urls)),
]