from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Website)
admin.site.register(DomainProviders)
admin.site.register(HostingProviders)
admin.site.register(Publishing)
admin.site.register(Company)
admin.site.register(WebsiteBusinessModel)
admin.site.register(WebsiteBusinesstype)


