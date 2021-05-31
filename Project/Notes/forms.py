from django import forms
from .models import Notes, NotesComments


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["name","subject","status","notes"]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = NotesComments
        fields = ["comment"]
