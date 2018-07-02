from django import forms
from .models import User, Sujet, Cours
# here your forms

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= '__all__'

class  SujetForm(forms.ModelForm):
    # dat= forms.DateField()

    class Meta:

        model= Sujet
        # fields= '__all__'
        fields= ('file', 'cours', 'domaine')

class   CoursForm(forms.ModelForm):

    class Meta:
        model= Cours
        fields= '__all__'
