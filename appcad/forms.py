from django import forms
from .models import Usuario

class FormCad(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields = ['nome', 'idade']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'NOME',
            'idade': 'IDADE',
        }