from rest_framework import serializers
from .models import AddValues

class GetAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AddValues
        fileds = '__all__'
        