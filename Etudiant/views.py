from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User, Sujet, Cours, Domaine
from django.generic.views import ListView
# Create your views here.

def user(request):

    thanx= False

    if request.method== "POST":
        
        form= UserForm(request.POST or None)
        
        if form.is_valid():
            pseaudo= form.cleaned_data['pseaudo']
            Email= form.cleaned_data['Email']

            thanx= True

            return redirect('Etudiant/inscription.html', {'thanx': thanx})
    else:
        form= UserForm()

    return render(request, 'Etudiant/inscription.html', {'form': form})


class List_Cour_et_Serie(ListView):
    model= Sujet
    template_name= "Base.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(ListCour, self).get_context_data(**kwargs)

        context['cours']= Cour.objects.all()

        context['domaine']= Domaine.objects.all()

        return context

class ListSujet((ListView):
    model= Sujet
    template_name= "base.html"
    context_object_name= "sujets"

    def get_queryset(self):
        return Sujet.objects.filter(Cours__id= self.kwargs['id'])

