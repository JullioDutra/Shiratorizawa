# forms.py
from django import forms
from .models import NewsletterSubscription

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Seu e-mail',
                'class': 'flex-grow px-4 py-3 rounded-l-full focus:outline-none text-gray-900'
            })
        }
