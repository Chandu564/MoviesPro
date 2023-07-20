from django.forms import ModelForm
from django import forms
from . models import Movie

class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
        widgets={
            'title' : forms.TextInput(attrs={'class':'inputfiled'}),
            'language' : forms.TextInput(attrs={'class': 'inputfiled'}),
            'poster': forms.FileInput(attrs={'class': 'inputfiled'}),
            'release_year': forms.NumberInput(attrs={'class': 'inputfiled'}),
            'lead_actor': forms.TextInput(attrs={'class': 'inputfiled'}),
            'rating': forms.NumberInput(attrs={'class': 'inputfiled'}),
        }