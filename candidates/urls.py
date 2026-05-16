from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ApplicantViewSet

r=DefaultRouter()
r.register('candidates',ApplicantViewSet)

urlpatterns =r.urls
