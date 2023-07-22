"""
URL configuration for bcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clinic_app.views import *

urlpatterns = [
    path('', include('chain.urls' )),
    path('website/', include('website_app.urls' )),
    path('user/', include('user_app.urls' )),
    path('article/', include('article_app.urls' )),
    path('clinic/', include('clinic_app.urls' )),
    path('admin/', admin.site.urls),
    path('select2/', include("django_select2.urls")),
    path('create_patient/', PatientCreateView.as_view(), name='create_patient'),
    path("__debug__/", include("debug_toolbar.urls")),
]
