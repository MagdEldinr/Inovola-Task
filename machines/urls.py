from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

r_machine = routers.DefaultRouter()
r_machine.register('',views.MachineViewSet)


urlpatterns = [
    path('api', include(r_machine.urls))
]