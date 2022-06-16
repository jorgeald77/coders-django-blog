from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


class ViewRegister(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form_register': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            nombre = form.cleaned_data.get('username')
            messages.success(request, f'Bievenido al Blog {nombre}')
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'register.html', {'form_register': form})


def salir(request):
    logout(request)
    messages.success(request, F'Haz finalizado la sesión')
    return redirect('home')
