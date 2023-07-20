from django import forms
from .models import *
from django.db.models import Q

class CreatePatientForm(forms.ModelForm):

    # qsbtype = WebsiteBusinesstype.objects.filter(
    #     WebsiteBusinessModel__company=business_model,
    # ) 
    clinic_qs = Clinic.objects.all()
    clinic = forms.ModelChoiceField(queryset=clinic_qs)
    c = clinic.get

    provider_qs = Provider.objects.filter(
        works_for_clinic_id=clinic.)
    

    provider = forms.ModelChoiceField(queryset=Provider.objects.none())




    class Meta:
        model = Patient
        fields = '__all__'

        