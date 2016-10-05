from django import forms
from .models import contact_form

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_form
        fields = ('name', 'email', 'message',)
