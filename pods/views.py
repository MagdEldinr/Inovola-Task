from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PodSerializer
from .models import Pod

# Create your views here.

class PodViewSet(viewsets.ModelViewSet):
    queryset = Pod.objects.all()
    serializer_class = PodSerializer
    filterset_fields = ['pod_type', 'pod_flavor', 'pod_pack_size']
    http_method_names = ['get']