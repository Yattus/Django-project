from django.shortcuts import HttpResponseRedirect, redirect, render
from .forms import InscriptionForm, SujetForm, ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Sujet, Cours, Domaine
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.


# View who display the inscription formulary
def inscription(request):

    if request.method == "POST":
        form = InscriptionForm(request.POST or None)

        if form.is_valid():
            pseaudo = form.cleaned_data['pseaudo']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(pseaudo, email,
                                            password, is_staff=True)

            return redirect("accueil")
    else:
        form = InscriptionForm()

    return render(request, 'Etudiant/inscription.html', locals())


# View who display the connexion formulary
def connexion(request):
    erros = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            pseaudo = form.cleaned_data['pseaudo']
            password = form.cleaned_data['password']
            # Nous verifions l'information fournis(s'il est inscrit)
            user = authenticate(username=pseaudo, password=password)
            if user:     # Si user est diff de none on le connect
                login(request, user)
            else:       # Sinon on affiche un message d'erreur
                erros = True
    else:
        form = ConnexionForm()

    return render(request, "Etudiant/connexion.html", locals())


# Generic View who display the formulary to add a subjet
class AjouterSujet(CreateView):
    model = Sujet
    template_name = "Etudiant/form_sujet.html"
    form_class = SujetForm
    success_url = reverse_lazy(connexion)

    # Redefine for add the field 'date' before save (define on html page)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.date = self.request.POST.get('date')
        self.object.save()

        # # for thanks the submitter to had the subjet
        # messages.success(self.request,
        #                       "Merci pour la contribution,\
        #                       le sujet à été ajouter avec succès")

        return HttpResponseRedirect(self.get_success_url())


# class Incription(CreateView):
#     model = User
#     template_name = "Etudiant/inscription.html"
#     form_class = InscriptionForm
#     success_url = reverse_lazy("Etudiant/form_sujet.html")


# View who display the list of Cours
class ListCours(ListView):
    model = Cours
    template_name = "Etudiant/list_cours.html"
    context_object_name = "cours"

    # Redefine queryset to precise the cours display
    def get_queryset(self):
        return Cours.objects.filter(domaine__id=self.kwargs['id'],
                                    domaine__slug=self.kwargs['slug'])

    # Redefine context to display in another color the domaine selected
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

    # Redefine queryset to precise the subjet display
    def get_queryset(self):
        return Sujet.objects.filter(cours__id=self.kwargs['id'],
                    cours__slug=self.kwargs['slug']).order_by('-date')

    # Redefine context to display in another color the domaine
    # and cours selected
    def get_context_data(self, **kwargs):

        context = super(ListSujet, self).get_context_data(**kwargs)

        context['cours'] = Cours.objects.filter(
                                    domaine__Nom=self.kwargs['Nom'])

        context['domainechoisie'] = Domaine.objects.get(Nom=self.kwargs['Nom'])

        context['courchoisie'] = Cours.objects.get(id=self.kwargs['id'],
                                                   slug=self.kwargs['slug'])

        return context
