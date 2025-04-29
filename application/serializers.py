from rest_framework import serializers
from . import models


class ApplicationSerializer(serializers.ModelSerializer):
    tuition = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Application
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    tuition = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Review
        fields = '__all__'
