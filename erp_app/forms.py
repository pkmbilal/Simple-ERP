from django import forms
from .models import Product

class productForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'bg-green-100 px-3 w-full h-10 outline-0','placeholder':'Product Name'}),
            'description': forms.Textarea(attrs={'class':'bg-green-100 block px-3 py-2 w-full h-20 outline-0','placeholder':'Product Description'}),
            'price': forms.TextInput(attrs={'class':'bg-green-100 block px-3 py-2 w-full h-10 outline-0','placeholder':'Price'}),
            'quantity': forms.TextInput(attrs={'class':'bg-green-100 block px-3 py-2 w-full h-10 outline-0','placeholder':'Quantity'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoryName'].empty_label = "Select an option"
        self.fields['categoryName'].widget.attrs.update({'class':'bg-green-100 w-full h-10 px-3 outline-0'})