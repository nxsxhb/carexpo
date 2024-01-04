from django import forms
from . models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=['brand_name', 'model_name', 'type', 'year', 'image']