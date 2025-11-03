from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['marca', 'modelo', 'descripcion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'ckeditor'}),
        }