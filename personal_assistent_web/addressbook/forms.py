from .models import Contact
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput, Select, EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone", 'birthday', "email", "address", ]
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя и фамилию'}),
            "phone": NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите phone'}),
            "birthday": DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите день рождения'}),
            "email": EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
            "address": Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Введите address'}),
            }