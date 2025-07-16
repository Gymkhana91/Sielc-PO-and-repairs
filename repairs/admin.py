from django.contrib import admin
from .models import Device, Configuration, Order

admin.site.register(Device)
admin.site.register(Configuration)
admin.site.register(Order)
