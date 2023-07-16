from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('', CoreDashboard.as_view(), name='core_dashboard'), 
    
]
