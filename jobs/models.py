from django.db import models

# Create your models here.
class Jobs(models.Model):
    title=models.CharField(max_length=20)
    required_skills=models.CharField(max_length=30)
    created_time=models.DateTimeField()
    