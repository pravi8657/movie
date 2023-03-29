from django import forms
from .models import table


class movieform(forms.ModelForm):
    class Meta:
        model = table
        fields = ['image', 'name', 'date', 'about']
