from django import forms
from .models import Movie,Genre
class MovieForm(forms.ModelForm):
    # Define the genres field as a multiple-choice field for selecting genres
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Movie
        fields = ['title','genre','director','imdb_rating']