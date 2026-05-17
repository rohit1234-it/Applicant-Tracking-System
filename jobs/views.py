from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .serializers import JobsSerializer
from .models import Jobs


# Create your views here
def home(request):
    jobs = Jobs.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})
    
class JobViewSet(viewsets.ModelViewSet):
    queryset=Jobs.objects.all()
    serializer_class=JobsSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
