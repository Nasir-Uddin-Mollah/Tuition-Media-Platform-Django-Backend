from rest_framework import serializers
from .import models


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = '__all__'


class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tuition
        fields = '__all__'
