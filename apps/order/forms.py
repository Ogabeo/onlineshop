from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['country', 'address', 'phone']
        widgets = {
            'country':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Country"}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Address"}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Phone"}),
        }