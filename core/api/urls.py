from home.views import index, people_create
from django.urls import path, include

urlpatterns = [
    path('index/', index),
    path('person/', people_create),
]