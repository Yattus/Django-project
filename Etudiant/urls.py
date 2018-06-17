from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns= [
    url(r'^accueil/', views.ListDomaine.as_view(template_name= 'Etudiant/accueil.html'), name= "accueil"),
    url(r'^informations/', TemplateView.as_view(template_name= "Etudiant/informations.html"), name= "informations"),
    url(r'^list_sujet/', views.ListSujet.as_view(), name= "list_sujet"),
    url(r'^list_cours/', views.ListCours.as_view(), name= "list_cours"),
    url(r'^ajouter_sujet/', views.ajouter_sujet, name= "ajouter_sujet"),
    url(r'^user$', views.user, name= 'connexion'),
]
