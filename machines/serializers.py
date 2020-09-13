from rest_framework import serializers

from .models import Machine

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        # fields = ['machine_name', 'machine_type', 'machine_model', 'water_compatible']
        fields = ['machine_name']