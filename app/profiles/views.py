from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class ViewProfile(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        # TODO Funcionalidad que muestra la info del usuario basada en su perfil
        return render(request, 'profile.html')

    def post(self, request):
        # TODO Funcionalidad para guardar o actualizar el registro.
        pass
