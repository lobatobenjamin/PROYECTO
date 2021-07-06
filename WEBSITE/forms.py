from django import forms
from django.forms import widgets
from .models import Product, Cart, CartDetail

class FormProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'category','image')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'requeried':'true', 'placeholder':'Título'}),
            'description' : forms.Textarea(attrs={'class': 'form-control form-control-sm', 'requeried':'true'}),
            'category' : forms.Select(attrs={'class': 'form-control form-control-sm', 'requeried':'true'}),
            'price' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'requeried':'true'}),
            'image' : forms.FileInput(attrs={'class': 'form-control form-control-sm', 'requeried':'true'})
        }
        
class FormCart(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('user', 'total')

class CartDetail(forms.ModelForm):

    class Meta:
        model = CartDetail
        fields = ('cart', 'product', 'quantity', 'price', 'total')
    
