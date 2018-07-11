# from django.contrib.signals import pre_delete
# from .models import Sujet
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^accueil/', views.ListDomaine.as_view(
    #     template_name='Etudiant/accueil.html'),
    #     name='accueil'
    #     ),

    url(r'^accueil/', TemplateView.as_view(
        template_name='Etudiant/accueil.html'),
        name='accueil'
        ),

    url(r'^informations/', TemplateView.as_view(
        template_name='Etudiant/informations.html'),
        name='informations'
        ),

    url(r'^list_sujet/(?P<id>\d+)-(?P<slug>.+)-(?P<Nom>.+)?$',
        views.ListSujet.as_view(),
        name='list_sujet'
        ),

    url(r'^ajouter_encors_un_sujet_ou_non.html/',
        TemplateView.as_view(
            template_name='Etudiant/ajouter_sujet_or.html'),
        name='ajouter_encors_un_sujet_ou_non'
        ),

    url(r'^list_cours/(?P<id>\d+)-(?P<slug>.+)',
        views.ListCours.as_view(),
        name='list_cours'
        ),

    url(r'^ajouter_sujet/', login_required(views.AjouterSujet.as_view(),
        login_url='/Etudiant/connexion/'),
        name="ajouter_sujet"
        ),

    url(r'^connexion/$', views.connexion, name='connexion'),
    
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),

    url(r'^inscription/$', views.inscription, name="inscription"),
    # url(r'^inscription$', views.Inscription.as_view(), name="inscription"),
]
