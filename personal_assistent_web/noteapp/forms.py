from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ["note", "tag"]
        widgets = {
            "note": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input here'
            }),
            "tag": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input here'
            }),
        }

# class NotesForm(ModelForm):
#     tag = forms.ModelChoiceField(queryset=TAG_CHOICES.objects.all())