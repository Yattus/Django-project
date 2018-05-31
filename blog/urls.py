from django.conf.urls import url
from django.urls import path, include
from blog import views
from .models import Article
from django.views.generic import ListView 



urlpatterns= [
    url(r'^$', ListView.as_view(
        model= Article,
                context_object_name= "articles",
                template_name= 'blog/accueil.html')),
    # url(r'^$', views.accueil, name='accueil'),
    url(r'^(?P<slug>.+)$', views.lire_article , name='blog_lire'),
]
