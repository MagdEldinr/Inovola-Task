from django.contrib import admin

from .models import Machine
# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    list_display = ['id', 'machine_name', 'machine_type', 'machine_model', 'water_compatible']


admin.site.register(Machine, MachineAdmin)