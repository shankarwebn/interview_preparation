from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, OrderViewSet,LoginView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('', include(router.urls)),
    
]