from django.db import models


class Order(models.Model):
    DEVICE_CHOICES = [
        ('xxz', 'LC'),
        ('GC-2020', 'GC-2020'),
        ('Prep Station', 'Prep Station'),
        ('HPLC-Plus', 'HPLC-Plus'),
    ]

    device = models.CharField(max_length=100, choices=DEVICE_CHOICES)
    configuration = models.TextField()
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.order_date} — {self.device} — {self.customer_name}"