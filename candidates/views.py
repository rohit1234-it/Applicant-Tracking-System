from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .models import Applicant
from .serializers import ApplicantSerializer

#for score logic
from jobs.models import Jobs
from candidates.serializers import ApplicantSerializer

#for notifications
from notifications.models import Notification


# Create your views here.
def candidates_page(request):
    candidates = Applicant.objects.all()
    return render(request, "candidates.html", {"candidates": candidates})

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset=Applicant.objects.all()
    serializer_class=ApplicantSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):

        candidate_name = request.data.get('candidate_name')
        email = request.data.get('email')
        skills = request.data.get('candidate_skills')
        job_id = request.data.get('applied_job')

        # fetch job
        job = Jobs.objects.get(id=job_id)

        # convert skills into list
        job_skills = [skill.strip().lower() for skill in job.required_skills.split(',')]

        candidate_skills = [skill.strip().lower() for skill in skills.split(',')]

        # matching count
        matched = 0

        for skill in candidate_skills:
            if skill in job_skills:
                matched += 1

        # percentage score
        score = (matched / len(job_skills)) * 100

        # save applicant
        applicant = Applicant.objects.create(
            candidate_name=candidate_name,
            email=email,
            candidate_skills=skills,
            score=score,
            applied_job=job
        )
        notification = Notification.objects.create( message=f"{candidate_name} applied for {job.title}",
       application=applicant)
        print(notification)
        
        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data)
    
    def get_queryset(self):
        min_score = self.request.query_params.get('score')
        if min_score:
            return Applicant.objects.filter(score__gte=min_score)
        return Applicant.objects.all().order_by('-score')
    
      