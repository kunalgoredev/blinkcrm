from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from .forms import *

# Create your views here.


class PatientCreateView(CreateView):
    model = Patient
    #fields = '__all__'
    form_class = CreatePatientForm
    template_name = 'clinic_app/create_patient.html'

    
    
    
    def get_success_url(self):
        return self.object.get_absolute_url()