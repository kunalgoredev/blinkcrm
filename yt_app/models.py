from django.db import models
from website_app.models import *

# Create your models here.


class Youtube(models.Model):
    channel_name = models.CharField(max_length=100, blank=True, null=True)
    website_associated = models.ForeignKey(Website, on_delete=models.PROTECT)
     