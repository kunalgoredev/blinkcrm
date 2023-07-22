from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *

# Create your views here.


class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    # form_class = createarticleForm
    template_name = 'article_app/create_article.html'

    
    
    
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