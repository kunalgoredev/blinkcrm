from django import forms
from .models import *


class createWebsiteForm(forms.ModelForm):

    # qsbtype = WebsiteBusinesstype.objects.filter(
    #     WebsiteBusinessModel__company=business_model,
    # ) 

    class Meta:
        model = Website
        fields = '__all__'

        