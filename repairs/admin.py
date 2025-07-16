from django.contrib import admin
from .models import Device, ConfigurationType, ConfigurationOption, Order

class ConfigurationOptionInline(admin.TabularInline):
    model = ConfigurationOption
    extra = 1

class ConfigurationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'device']
    inlines = [ConfigurationOptionInline]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'device', 'customer_name']
    filter_horizontal = ('configurations',)  # чтобы удобно выбирать много конфигураций

admin.site.register(Device)
admin.site.register(ConfigurationType, ConfigurationTypeAdmin)
admin.site.register(ConfigurationOption)
admin.site.register(Order, OrderAdmin)
