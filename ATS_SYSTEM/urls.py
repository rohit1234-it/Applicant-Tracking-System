from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    #jobs
     path('', include('jobs.urls')),          # HTML
    path('api/', include('jobs.api_urls')),
    #candidates 
    path('candidates/', include('candidates.urls')),
    path('api/', include('candidates.api_urls')),
    #notifications
    path('notifications/', include('notifications.urls')),
    path('api/',include('notifications.api_urls')),

    # JWT
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]