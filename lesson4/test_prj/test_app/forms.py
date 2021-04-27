from .models import GoodItem
from django import forms

class AddForm(forms.ModelForm):
    class Meta:
        model = GoodItem
        fields = ('name', 'description', 'quantity')
