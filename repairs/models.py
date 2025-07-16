from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Configuration(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    configuration = ChainedForeignKey(
        Configuration,
        chained_field="device",
        chained_model_field="device",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
    )

    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.order_date} — {self.device} — {self.customer_name}"