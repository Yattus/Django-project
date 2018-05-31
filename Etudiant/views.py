from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
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
