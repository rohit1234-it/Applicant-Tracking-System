from django.db import models
from candidates.models import Applicant

# Create your models here.
class Notification(models.Model):
    message=models.CharField(max_length=100)
    read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    application=models.ForeignKey(Applicant,on_delete=models.CASCADE)