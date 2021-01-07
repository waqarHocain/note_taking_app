from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "title",
            "body",
        )
        widgets = {
            "title": forms.fields.TextInput(attrs={"placeholder": "Enter note title"}),
            "body": forms.fields.Textarea(attrs={"placeholder": "Enter note content"}),
        }
