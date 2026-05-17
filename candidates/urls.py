from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicantViewSet, candidates_page

router = DefaultRouter()
router.register('candidates', ApplicantViewSet)

urlpatterns = [
    path('', candidates_page),          
    path('api/', include(router.urls)), 
]