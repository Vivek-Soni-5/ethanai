from django import forms
from .models import Financial

class financialForm(forms.ModelForm):
    
    class Meta:
        model = Financial
        fields = "__all__"