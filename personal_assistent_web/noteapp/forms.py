from .models import Notes
from django.forms import ModelForm, TextInput, Textarea


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