from django.contrib import admin
from .models import Order, RepairAndService  # Оставим только нужное

admin.site.register(Order)
admin.site.register(RepairAndService)
