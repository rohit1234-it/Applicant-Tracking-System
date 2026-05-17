from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet,job_page

r=DefaultRouter()
r.register('jobs',JobViewSet)

urlpatterns = [
    path('', job_page),

    # API
    path('api/', include(r.urls)),
]