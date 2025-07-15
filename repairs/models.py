from django.db import models

class Order(models.Model):
    device = models.CharField(max_length=100)
    configuration = models.TextField()
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.order_date} — {self.device} — {self.customer_name}"