from django import forms
from .models import User, Exercise, Cour
# here your forms

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= '__all__'

class   ExerciseForm(forms.ModelForm):
    class Meta:
        model= Exercise
        fields= '__all__'

class   CourForm(forms.ModelForm):
    class Meta:
        model= Cour
        fields= '__all__'
