from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns= [
    url(r'^accueil$', views.ListDomaine.as_view(template_name= 'Etudiant/accueil.html'), name= "accueil"),
    url(r'^informations$', views.ListDomaine.as_view(template_name= "Etudiant/informations.html"), name= "informations"),
    url(r'^user$', views.user, name= 'connexion'),
]
