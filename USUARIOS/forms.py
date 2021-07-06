from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class':'usuario'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y solamente.')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Al menos 8 caracteres y no pueden ser solo numeros.')
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Ingrese la misma contraseña de antes para la verificación.')
    email = forms.CharField(label='Email', widget=forms.EmailInput(), max_length=254, required=True, help_text='Se requiere una dirección de email válida.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'groups']