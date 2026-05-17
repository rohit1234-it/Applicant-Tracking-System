from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicantViewSet, candidates_page

router = DefaultRouter()

# IMPORTANT: empty prefix inside app
router.register(r'', ApplicantViewSet)

urlpatterns = [
    path('', candidates_page),   
    ]