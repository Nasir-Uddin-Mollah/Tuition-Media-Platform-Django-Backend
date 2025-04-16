from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('list', views.TuitionViewSet)
router.register('class', views.ClassViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
