from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^accueil/', views.ListDomaine.as_view(template_name='Etudiant/accueil.html'), name='accueil'),
    url(r'^informations/', TemplateView.as_view(template_name='Etudiant/informations.html'), name='informations'),
    url(r'^list_sujet/(?P<id>\d+)$', views.ListSujet.as_view(), name='list_sujet'),
    url(r'^ajouter_sujet_or.html/', TemplateView.as_view(template_name='Etudiant/ajouter_sujet_or.html'), name='ajouter_sujet_or'),
    url(r'^list_cours/(?P<id>\d+)$', views.ListCours.as_view(), name='list_cours'),
    url(r'^ajouter_sujet/', views.ajouter_sujet, name="ajouter_sujet"),
    url(r'^user$', views.user, name='connexion'),
]
