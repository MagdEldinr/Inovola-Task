from django.db import models

from .choices import type_choices, pack_size_choices, flavor_choices
# Create your models here.

class Pod(models.Model):
    pod_name = models.CharField(max_length=5, unique=True)
    pod_type = models.CharField(choices=type_choices, max_length=10)
    pod_flavor = models.CharField(choices=flavor_choices, max_length=10)
    pod_pack_size = models.IntegerField(choices=pack_size_choices)

    def __str__(self):
        return self.pod_name
    