from django import forms
from .models import Contacts


class FormContactItem(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name', 'address', 'phone', 'email']