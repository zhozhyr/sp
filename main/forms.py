from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    phone = forms.CharField(max_length=20, validators=[
        RegexValidator(
            regex=r'^(\+7|8)?\d{10}$',
            message="Введите номер в формате +71234567890/81234567890"
        ),
    ])

    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)