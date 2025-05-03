from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from tuition.models import Tuition


class ApplicationSerializer(serializers.ModelSerializer):
    tuition = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Application
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    tuition_details = serializers.SerializerMethodField()

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    tuition = serializers.PrimaryKeyRelatedField(
        queryset=Tuition.objects.all())

    class Meta:
        model = models.Review
        fields = '__all__'

    def get_user_details(self, obj):
        user = obj.user
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

    def get_tuition_details(self, obj):
        tuition = obj.tuition
        return {
            "id": tuition.id,
            "title": tuition.title,
            "subject": tuition.subject,
            "class_name": tuition.class_name.name,
            "description": tuition.description,
            "is_available": tuition.is_available,
        }
