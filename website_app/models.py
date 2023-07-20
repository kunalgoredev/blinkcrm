from django.db import models
from core_app.models import BaseModel
from django.urls import reverse
# Create your models here.



class DomainProviders(models.Model):
    provider_name = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.provider_name



class HostingProviders(models.Model):
    provider_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.provider_name


class Publishing(models.Model):

    publishing_frequency = models.CharField(max_length=20, blank=True, null=True)
    publishing_day = models.CharField(max_length=20, blank=True, null=True)
    publishing_per = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return self.publishing_frequency


class Company(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    company_contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.company_name

class WebsiteBusinessModel(models.Model):
    business_model = models.CharField(max_length=100, blank=True, null=True)
    business_company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.business_model
    

class WebsiteBusinesstype(models.Model):
    business_name = models.CharField(max_length=100, blank=True, null=True)
    model_type = models.ForeignKey(WebsiteBusinessModel, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.business_name



class Website(BaseModel):


    # DOMAIN_PROVIDER_CHOICES = (
    # ("Dynadot", "Dynadot"),
    # ("GoDaddy", "GoDaddy"),
    # ("IONOS", "IONOS"),
    # )
    
    # HOSTING_PROVIDER_CHOICES = (
    # ("DigitalOcean", "DigitalOcean"),
    # ("Hostinger", "Hostinger"),
    # ("Bluehost", "Bluehost"),
    
    # )

    FREQUENCY_PUBLISHING = (
        ('OnceDaily', 'OnceDaily'),
        ('4/Week', '4/Week'),
    )



    website_name = models.CharField(max_length=50, null=True, blank=True)
    website_url = models.URLField(max_length=100, null=True, blank=True)
    admin_website = models.CharField(max_length=100, null=True, blank=True)
    user_website = models.CharField(max_length=100, null=True, blank=True)
    admin_pass = models.CharField(max_length=100, null=True, blank=True)
    user_pass = models.CharField(max_length=100, null=True, blank=True)
    email_website = models.EmailField(max_length=100, null=True, blank=True)
    email_pass = models.CharField(max_length=100, null=True, blank=True)

    domain_provider = models.ForeignKey(DomainProviders, null=True, blank=True, on_delete=models.PROTECT) 
    hosting_provider = models.ForeignKey(HostingProviders, null=True, blank=True, on_delete=models.PROTECT) 
    publishing_frequency = models.CharField(max_length=20, choices=FREQUENCY_PUBLISHING, default='OnceDaily')
    #website_business = models.ForeignKey(WebsiteBusinessModel, null=True, blank=True, on_delete=models.PROTECT)
    

    def get_absolute_url(self):
        return reverse('website_app:website_detail', args=[str(self.id)])

    def __str__(self):
        return self.website_name

