from rest_framework import serializers

from .models import Pod

class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        # fields = ['pod_name', 'pod_type', 'pod_flavor', 'pod_pack_size']
        fields = ['pod_name']
