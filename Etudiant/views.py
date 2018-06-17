from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm, SujetForm
from .models import User, Sujet, Cours, Domaine
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# Create your views here.

def user(request):

    thanx= False

    if request.method== "POST":
        
        form= UserForm(request.POST or None)
        
        if form.is_valid():
            pseaudo= form.cleaned_data['pseaudo']
            Email= form.cleaned_data['Email']

            thanx= True

            return redirect('Etudiant/Connexion.html', {'thanx': thanx})
    else:
        form= UserForm()

    return render(request, 'Etudiant/Connexion.html', {'form': form})

def ajouter_sujet(request):
    ok= False
    
    form= SujetForm(request.POST or None, request.FILES)

    if form.is_valid():
        sujet= Sujet()
        sujet= form.save(commit= False)
        sujet.save()
        ok= True
    
        # return render(request, "Etudiant/form_sujet.html", {'form': form, 'ok': ok})
        return redirect('accueil')

    else:
        form= SujetForm()

    return redirect('accueil')

#List_Cour_et_Serie was his name is changed now by ListDomaine
# View who display list of fileds 
class ListDomaine(ListView):
    model= Domaine
    context_object_name= "domaines"
    template_name= "Etudiant/accueil.html"
    
    def get_queryset(self):
        return Domaine.objects.all()

# View who display the list of Cours
class ListCours(ListView):
    model= Cours
    template_name= "Etudaint/list_cours.html"
    context_object_name= "cours"

    def get_queryset(self):
        return Cours.objects.filter(Domaine__id= self.kwargs['id'])

# View who display the list Subjet
class ListSujet(ListView):
    model= Sujet
    template_name= "Etudiant/list_sujet.html"
    context_object_name= "sujets"

    def get_queryset(self):
        return Sujet.objects.filter(Cours__id= self.kwargs['id'])


# View who display only one sujet to read
class LireSujet(DetailView):
    model= Sujet
    context_object_name= "sujet"
    template_name= "Etudiant/lire_sujet.html"

    def get_object(self):
        # We get the thing for super class
        sujet= super(LireSujet, self).get_object()

        # we increase the number view
        sujet.nb_View+= 1

        return sujet    #we return l'objet to read

# Je devais creer un template pour le formulaire d'ajoute de sujet qui à ete fais et donc 
# je devais faire une views pour affciher le formulaire d'ajoute de sujet afin de voir
# comment on peut ajouter une date du sujet et ensuite afficher le sujet

