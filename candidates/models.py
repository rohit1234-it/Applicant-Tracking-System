from django.db import models
from jobs.models import Jobs

# Create your models here.
class Applicant(models.Model):
    candidate_name=models.CharField(max_length=55)
    email=models.EmailField(max_length=55)
    candidate_skills=models.CharField(max_length=55)
    score=models.FloatField(blank=True,null=True)
    applied_job=models.ForeignKey(Jobs, on_delete=models.CASCADE) 
    
    def save(self, *args, **kwargs):
        if self.candidate_skills:
            self.score = len(self.candidate_skills.split(",")) * 10
        super().save(*args, **kwargs)