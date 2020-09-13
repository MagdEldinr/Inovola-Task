from django.db import models

from .choices import model_choices, type_choices
# Create your models here.

class Machine(models.Model):

    machine_name = models.CharField(max_length=5, unique=True)
    machine_type = models.CharField(choices=type_choices, max_length=10, blank=True)
    machine_model = models.CharField(choices=model_choices, max_length=10, blank=True)
    water_compatible = models.BooleanField()

    def __str__(self):
        return self.machine_name
    
    
