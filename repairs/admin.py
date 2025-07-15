from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'device', 'customer_name')
    search_fields = ('device', 'customer_name')
    list_filter = ('order_date',)
