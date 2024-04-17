# drowsiness_detection/urls.py
from django.urls import path
from . import views
from .views import drowsiness_detection

urlpatterns = [
     path('drowsiness-detection/', drowsiness_detection, name='drowsiness_detection'),
]