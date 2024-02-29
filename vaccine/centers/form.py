from django import forms 
from .models import VaccineCenter

class ProductForm(forms.ModelForm):
    class Meta:
        model=VaccineCenter
        fields=['name','address','phone','email','starttime','endtime','capacity','description']
        