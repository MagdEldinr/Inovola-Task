from django.contrib import admin

from .models import Pod
# Register your models here.
class PodAdmin(admin.ModelAdmin):
    list_display = ['id', 'pod_name', 'pod_type', 'pod_flavor', 'pod_pack_size']


admin.site.register(Pod, PodAdmin)