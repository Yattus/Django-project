from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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

            return redirect('Etudiant/Connexion.html', {'thanx': thanx})
    else:
        form = UserForm()

    return render(request, 'Etudiant/Connexion.html', {'form': form})


def ajouter_sujet(request):
    # for a message to thanx add of subjet
    ok = False

    form = get_object_or_404(SujetForm(request.POST or None, request.FILES))

    if form.is_valid():
        sujet = Sujet()
        sujet = form.save(commit=False)
        sujet.date = request.POST.get('date')
        sujet.save()
        ok = True

        # return render(request, "Etudiant/form_sujet.html",
        # {'form': form, 'ok': ok})
        return redirect('ajouter_sujet_or')

    else:
        form = get_object_or_404(SujetForm)

    return render(request,
                  'Etudiant/form_sujet.html',
                  {'form': form, 'ok': ok})


# List_Cour_et_Serie was his name is changed now by ListDomaine
# View who display list of fileds
class ListDomaine(ListView):
    model = Domaine
    context_object_name = "domaines"
    template_name = "Etudiant/accueil.html"

    def get_queryset(self):
        return get_list_or_404(Domaine.objects.all())


# View who display the list of Cours
class ListCours(ListView):
    model = Cours
    template_name = "Etudiant/list_cours.html"
    context_object_name = "cours"
    # cour = Cours.objects.filter(domaine__id= .kwargs['id'])

    def get_queryset(self):
        return get_list_or_404(Cours.objects.filter(
            domaine__id=self.kwargs['id']))

    def get_context_data(self, **kwargs):

        context = super(ListCours, self).get_context_data(**kwargs)

        context['domaine'] = get_object_or_404(Domaine,
                                               id=self.kwargs['id'])

        context['domaines'] = get_list_or_404(Domaine.objects.all())

        return context


# View who display the list Subjet
class ListSujet(ListView):
    model = Sujet
    template_name = "Etudiant/list_sujet.html"
    context_object_name = "sujets"

    def get_queryset(self):
        return get_list_or_404(Sujet.objects.filter(
            cours__id=self.kwargs['id']).order_by('-date'))

    def get_context_data(self, **kwargs):

        context= super(ListSujet, self).get_context_data(**kwargs)

        context['domaines']= get_list_or_404(Domaine.objects.all())

        return context
