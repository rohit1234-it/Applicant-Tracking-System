from rest_framework import serializers
from .models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    
    applied_job = serializers.SerializerMethodField()
    
    
    class Meta:
        fields='__all__'
        model=Applicant
        
        
    def get_applied_job(self, obj):
            if obj.applied_job:
                return {
                "id": obj.applied_job.id,
                "title": obj.applied_job.title
                }
            return None