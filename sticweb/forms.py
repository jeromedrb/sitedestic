
from django import forms
from .models import Message, Usersinfo, demandesolution

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'telephone', 'message']
        labels = {"name": "Nom" }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Usersinfo
        fields = ['name', 'email', 'tel']

class DemandeSolutionForm(forms.ModelForm):
    class Meta:
        model = demandesolution
        fields = ['demandeur_id', 'solutiondemande_id']