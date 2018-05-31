from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        # fields= ('Pseaudo', 'Email', 'contenu')
        exclude= ('articleComment',)

