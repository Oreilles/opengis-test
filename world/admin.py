from django.contrib.gis import admin

from .models import Pipe, Valve

admin.site.register(Pipe, admin.ModelAdmin)
admin.site.register(Valve, admin.ModelAdmin)
