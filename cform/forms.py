from django import forms
from .models import cred

class credform(forms.ModelForm):
    class Meta:
        model=cred
        fields=('firstname','lastname',)
