from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=220)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, default=False, null=True)
    date = models.DateTimeField(blank=False, default=timezone.now, null=True)

    @property
    def get_discount(self):
        return "%.2f" % (float(self.price) * 0.5)