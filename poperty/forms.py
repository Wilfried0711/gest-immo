from django import forms
from .models import Poperty

class PopertyForm(forms.ModelForm):
    class Meta:
        model = Poperty
        fields = ['name', 'description','price','superficy','type','image','bedrooms','bathrooms','owner_id' ]