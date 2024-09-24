from django import forms
from .models import Item


class FormContactItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['first_name', 'last_name', 'address', 'phone', 'email']