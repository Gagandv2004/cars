from django import forms
from cbvapp.models import Products

class EMIFORM(forms.ModelForm):
    product_name=forms.CharField(disabled=True)
    company=forms.CharField(disabled=True)
    price=forms.CharField(disabled=True)
    class Meta:
        model=Products
        fields=['product_name','company','price']