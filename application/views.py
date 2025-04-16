from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.


class ApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        application_id = self.request.query_params.get('application_id')
        user_id = self.request.query_params.get('user_id')

        if application_id:
            queryset = queryset.filter(id=application_id)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        tuition_id = self.request.query_params.get('tuition_id')
        user_id = self.request.query_params.get('user_id')
        
        if tuition_id:
            queryset = queryset.filter(tuition_id=tuition_id)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
