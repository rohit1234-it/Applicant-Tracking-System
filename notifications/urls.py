from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet,notification_page

router = DefaultRouter()
router.register('notifications',NotificationViewSet)

urlpatterns = [
    path('', notification_page),          
    path('api/', include(router.urls)), 
]