from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet

r=DefaultRouter()
r.register('notifications',NotificationViewSet)

urlpatterns =r.urls
