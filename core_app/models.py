from django.db import models
import uuid

# Create your models here.


class BaseModel(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )

    PUBLISHING_STATUS_CHOICES = (
        ('Live', 'Live'),    
        ('Publishing', 'Publishing'),    
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    publishing_status = models.CharField(max_length=20,choices=PUBLISHING_STATUS_CHOICES, default='Live')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', blank=True)
    
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
