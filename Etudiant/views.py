from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User, Sujet, Cours, Domaine
from django.views.generic import ListView
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

#List_Cour_et_Serie was his name is changed now by ListDomaine
# Vue who display list of fileds 
class ListDomaine(ListView):
    model= Domaine
    context_object_name= "domaines"
    template_name= "Etudiant/accueil.html"
    
    def get_queryset(self):
        return Domaine.objects.all()

# Vue who display the list of Cours
class ListCours(ListView):
    model= Cours
    template_name= "Etudaint/list_cours.html"
    context_object_name= "cours"

    def get_queryset(self):
        return Cours.objects.filter(Domaine__id= self.kwargs['id'])

# Vue who display the list Subjet
class ListSujet(ListView):
    model= Sujet
    template_name= "Etudiant/accueil.html"
    context_object_name= "sujets"

    def get_queryset(self):
        return Sujet.objects.filter(Cours__id= self.kwargs['id'])

