from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.order_date} — {self.device} — {self.customer_name}"
