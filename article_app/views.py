from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from django.contrib import messages
# Create your views here.


class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    # form_class = createarticleForm
    template_name = 'article_app/create_article.html'

    def form_valid(self, form):
        messages.info(self.request, 'Article created successfully')
        return super().form_valid(form)
    
    
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    

class ArticleListView(ListView):
    model = Article
    template_name = "article_app/article_list.html"
    context_object_name = 'article'    



class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'article_app/article_detail.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def form_valid(self, form):
        messages.info(self.request, 'Article Updated successfully')
        return super().form_valid(form)