from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .models import Applicant
from .serializers import ApplicantSerializer
from jobs.models import Jobs
from notifications.models import Notification


# UI page
def candidates_page(request):
    candidates = Applicant.objects.all()
    return render(request, "candidates.html", {"candidates": candidates})


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):

        candidate_name = request.data.get('candidate_name')
        email = request.data.get('email')
        skills = request.data.get('candidate_skills')
        job_id = request.data.get('applied_job')

        # fetch job safely
        job = Jobs.objects.get(id=job_id)

        # normalize skills
        job_skills = set([
            skill.strip().lower()
            for skill in job.required_skills.split(',')
            if skill.strip()
        ])

        candidate_skills = set([
            skill.strip().lower()
            for skill in skills.split(',')
            if skill.strip()
        ])

        # scoring logic
        if len(job_skills) == 0:
            score = 0
        else:
            matched = job_skills.intersection(candidate_skills)
            score = (len(matched) / len(job_skills)) * 100
            score = round(score, 2)

        # save applicant
        applicant = Applicant.objects.create(
            candidate_name=candidate_name,
            email=email,
            candidate_skills=skills,
            applied_job=job,
            score=score
        )

        # notification
        Notification.objects.create(
            message=f"{candidate_name} applied for {job.title}",
            application=applicant
        )

        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data)

    def get_queryset(self):
        min_score = self.request.query_params.get('score')

        if min_score:
            return Applicant.objects.filter(score__gte=min_score)

        return Applicant.objects.all().order_by('-score')