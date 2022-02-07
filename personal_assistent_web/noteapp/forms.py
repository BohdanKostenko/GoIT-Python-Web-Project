from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class NotesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'].empty_label = "Choose category"

    class Meta:
        model = Notes
        fields = ["tag","note"]
        widgets = {
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input here'})
        }


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'].empty_label = "Choose category"


class ChoiceForm(forms.Form):
    name = forms.ChoiceField(label='Select Tag')


# class NotesForm(ModelForm):
#     class Meta:
#         model = Notes
#         fields = ["note", "tag"]
#         widgets = {
#             "note": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Input here'
#             }),
#             "tag": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Input here'
#             }),
