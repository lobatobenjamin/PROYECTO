from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


from WEBSITE.models import Category

def registrarse(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Se ha registrado el usuario " + user)
                return redirect('login')

        return render(request,'registration/registro.html', 
            {'form' : form, "lista_categorias" : Category.objects.all()}
        )
