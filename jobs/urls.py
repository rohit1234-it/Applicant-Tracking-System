from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

r=DefaultRouter()
r.register('jobs',JobViewSet)

urlpatterns =r.urls
