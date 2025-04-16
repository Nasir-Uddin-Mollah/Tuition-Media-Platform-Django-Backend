from django.shortcuts import render
from rest_framework import viewsets
from .import serializers
from .import models
from rest_framework import filters, pagination
# Create your views here.


class ClassViewSet(viewsets.ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = models.Tuition.objects.all()
    serializer_class = serializers.TuitionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['class_name__name']
