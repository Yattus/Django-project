from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns= [
    url(r'^accueil$', TemplateView.as_view(template_name= 'Etudiant/acceuil.html'), name= "accueil"),
    url(r'^informations$', TemplateView.as_view(template_name= "Etudiant/informations.html"), name= "informations"),
    url(r'^user$', views.user, name= 'inscription'),
]