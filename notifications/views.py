from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer


# Create your views here.
def notification_page(request):
    return render(request, "notifications.html")


class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

  