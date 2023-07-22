from django.db import models

# Create your models here.
from django.db import models
from core_app.models import BaseModel
from auditlog.registry import auditlog
from django.urls import reverse
# Create your models here.


class Article(BaseModel):

    writer_name = models.CharField(max_length=150, blank=True,null=True)
    writer_status = models.CharField(max_length=200, blank=True, null=True)
    # price_per_word = models.FloatField(
    

  

    def get_absolute_url(self):
        return reverse('article_app:article_detail', args=[str(self.id)])
    def __str__(self):
        return self.article_name






auditlog.register(Article)