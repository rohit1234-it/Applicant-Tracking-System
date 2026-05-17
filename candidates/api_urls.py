from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicantViewSet

router = DefaultRouter()
router.register(r'candidates', ApplicantViewSet)

urlpatterns = router.urls