from rest_framework import serializers
from .models import Jobs

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Jobs

        