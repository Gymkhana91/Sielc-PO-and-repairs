from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ConfigurationType(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.device.name} – {self.name}"


class ConfigurationOption(models.Model):
    config_type = models.ForeignKey(ConfigurationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.config_type.name}: {self.name}"


class Order(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    configurations = models.ManyToManyField(ConfigurationOption)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.order_date} — {self.device} — {self.customer_name}"
