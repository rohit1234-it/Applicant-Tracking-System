from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .models import Applicant
from .serializers import ApplicantSerializer
from jobs.models import Jobs
from notifications.models import Notification


def candidates_page(request):
    candidates = Applicant.objects.all()
    return render(request, "candidates.html", {"candidates": candidates})


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):

        candidate_name = request.data.get('candidate_name')
        email = request.data.get('email')
        skills = request.data.get('candidate_skills')
        job_id = request.data.get('applied_job')
        job = Jobs.objects.get(id=job_id)
        
        def logic(skills):
            return skills.strip().lower().replace('.', '').replace(' ', '')
        
        candidate_skills = {logic(s) for s in skills.split(',') if s.strip()}
        job_skills = {logic(s) for s in job.required_skills.split(',') if s.strip()}

        matched=candidate_skills & job_skills
        missing = job_skills - candidate_skills

        score = round((len(matched) / len(job_skills)) * 100, 2)
        print(score)
        applicant = Applicant.objects.create(
            candidate_name=candidate_name,
            email=email,
            candidate_skills=skills,
            score=score,
            applied_job=job,
        )

        Notification.objects.create(
            message=f"{candidate_name} applied for {job.title}",
            application=applicant
        )
        
        return Response({
            "applied_job": {
            "id": job.id,
            "title": job.title
            },
            "score": score
            })

    def get_queryset(self):
        return Applicant.objects.all().order_by('-score','-id')