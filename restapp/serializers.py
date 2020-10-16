from rest_framework import serializers
from .models import General_detail

class General_detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = General_detail
        fields = '__all__'
        