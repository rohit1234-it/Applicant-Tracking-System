from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, home

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', home),                 # UI page
]