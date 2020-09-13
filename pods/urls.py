from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

r_pod = routers.DefaultRouter()
r_pod.register('',views.PodViewSet)


urlpatterns = [
    path('api', include(r_pod.urls))
]