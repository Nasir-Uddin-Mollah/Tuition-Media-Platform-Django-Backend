from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('list', views.ApplicationViewset)
router.register('review/list', views.ReviewViewset)
urlpatterns = [
    path('', include(router.urls)),
]
