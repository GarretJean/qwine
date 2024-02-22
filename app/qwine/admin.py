from django.contrib import admin

from .models import Cave, Cepage, Inventaire, Vin

admin.site.register(Vin)
admin.site.register(Cepage)
admin.site.register(Inventaire)
admin.site.register(Cave)
