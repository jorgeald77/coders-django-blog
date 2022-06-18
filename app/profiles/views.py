from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from profiles.forms import FormProfile


class ViewProfile(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form_profile = FormProfile(instance=request.user.profile)
        return render(request, 'profile.html', {'form': form_profile, 'has_foto': form_profile['foto'].value()})

    def post(self, request):
        form_profile = FormProfile(request.POST, request.FILES, instance=request.user.profile)
        if form_profile.is_valid():
            user = request.user
            user.first_name = form_profile.cleaned_data['nombre']
            user.last_name = form_profile.cleaned_data['apellidos']
            user.save()

            form_profile.save()
            messages.success(request, f'Perfil actualizado')
            return redirect('profile')
