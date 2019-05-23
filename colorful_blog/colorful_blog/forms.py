from django import forms

class ContactForm(forms.Form):
    client_name: forms.CharField()
    client_email: forms.CharField()
    client_requirements: forms.CharField()