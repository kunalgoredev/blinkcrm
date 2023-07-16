from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
# Create your views here.





class WebsiteListView(ListView):
    model = Website
    template_name = "website_app/website_list.html"
    context_object_name = 'website'

    # def get_queryset(self, *args, **kwargs):
    #     # qs = super(WebsiteListView, self).get_queryset(*args, **kwargs)
    #     qs = {'all': qs.objects.all(),
    #           'active': qs.objects.filter(status='Active')
    #           }
              

        
    #     return qs



class WebsiteCreateView(CreateView):
    model = Website
    fields = '__all__'
    template_name = 'core_app/create_site.html'
    
    
    
    def get_success_url(self):
        return reverse('core_app:update_site')
    


class WebsiteUpdateView(UpdateView):
    model = Website
    fields = '__all__'

    template_name = "website_app/website_detail.html"

    
   
   
    def get_success_url(self):
        return self.object.get_absolute_url()
    
    # def form_valid(self, form):
    #     messages.success(self.request, f'Save Completed ! Site has been updated')
    #     return super().form_valid(form)
