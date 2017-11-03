from django.db import models
from datetime import *

class Sites(models.Model):

    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField( max_length=20,unique=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Site Name"

class SiteData(models.Model):

    site  = models.ForeignKey(Sites)
    record_date = models.DateField()
    a_value = models.DecimalField(max_digits=10, decimal_places=2)
    b_value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Site Values"
