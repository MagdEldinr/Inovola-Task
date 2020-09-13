from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MachineSerializer
from .models import Machine
# Create your views here.


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filterset_fields = ['machine_type', 'machine_model', 'water_compatible']
    http_method_names = ['get']
