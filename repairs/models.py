from django.db import models


class Order(models.Model):
    DEVICE_CHOICES = [
        ('Alltesta Gradient', 'Alltesta Gradient'),
        ('Alltesta Isocratic', 'Alltesta Isocratic'),
        ('Cromite Isocratic', 'Cromite Isocratic'),
        ('Cromite Gradient', 'Cromite Gradient'),
        ('OEM Autosampler', 'OEM Autosampler'),
        ('OEM Syringe Pump HPLC', 'OEM Syringe Pump HPLC'),
        ('OEM UV Detector', 'OEM UV Detector'),
        ('Standalone Syringe', 'Standalone Syringe'),
        ('Standalone Valve', 'Standalone Valve'),
    ]

    device = models.CharField(max_length=100, choices=DEVICE_CHOICES)
    configuration = models.TextField()
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.order_date} — {self.device} — {self.customer_name}"