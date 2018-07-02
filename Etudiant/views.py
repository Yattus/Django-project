from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import UserForm, SujetForm
from .models import Sujet, Cours, Domaine
from django.views.generic import ListView
# DetailView, CreateView
# from django.urls import reverse_lazy
# Create your views here.


def user(request):

    thanx = False

    if request.method == "POST":

        form = UserForm(request.POST or None)

        if form.is_valid():
            pseaudo = form.cleaned_data['pseaudo']
            Email = form.cleaned_data['Email']

            thanx = True

            return redirect('Etudiant/Connexion.html',
                            {'thanx': thanx})
    else:
        form = UserForm()

    return render(request,
                  'Etudiant/Connexion.html',
                  {'form': form})


def ajouter_sujet(request):
    # for a message to thanx add of subjet
    ok = False

    form = SujetForm(request.POST or None, request.FILES)

    if form.is_valid():
        sujet = get_object_or_404(Sujet)
        sujet = form.save(commit=False)
        sujet.date = request.POST.get('date')
        sujet.save()
        ok = True

        # return render(request, "Etudiant/form_sujet.html",
        # {'form': form, 'ok': ok})
        return redirect('ajouter_sujet_or')

    else:
        form = SujetForm()

    return render(request,
                  'Etudiant/form_sujet.html',
                  {'form': form, 'ok': ok})


# View who display the list of Cours
class ListCours(ListView):
    model = Cours
    template_name = "Etudiant/list_cours.html"
    context_object_name = "cours"

    def get_queryset(self):
        return Cours.objects.filter(domaine__id=self.kwargs['id'],
                                    domaine__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):

        context = super(ListCours, self).get_context_data(**kwargs)

        context['domainechoisie'] = Domaine.objects.get(
                                            id=self.kwargs['id'],
                                            slug=self.kwargs['slug'])

        return context


# View who display the list Subjet
class ListSujet(ListView):
    model = Sujet
    template_name = "Etudiant/list_sujet.html"
    context_object_name = "sujets"

    def get_queryset(self):
        return Sujet.objects.filter(cours__id=self.kwargs['id'],
                    cours__slug=self.kwargs['slug']).order_by('-date')

    def get_context_data(self, **kwargs):

        context = super(ListSujet, self).get_context_data(**kwargs)

        context['cours'] = Cours.objects.filter(
                                    domaine__Nom=self.kwargs['Nom'])

        context['domainechoisie'] = Domaine.objects.get(Nom=self.kwargs['Nom'])

        context['courchoisie'] = Cours.objects.get(id=self.kwargs['id'],
                                                   slug=self.kwargs['slug'])

        return context
