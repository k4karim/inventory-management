from django import forms

from .models import Inventory

class MedForm(forms.ModelForm):

    class Meta:
        model=Inventory
        fields=('prod_title','quantity',)

        widgets={
            'prod_title':forms.TextInput(attrs={'class':'form-control',"placeholder": "Enter Post title",'required':True,}),
            'quantity':forms.NumberInput(attrs={'class':'form-control z-depth-1',"placeholder": "Write Post here",'required':True,}),

            }



