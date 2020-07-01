from django import forms
from customer.models import Customer

class CusForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'