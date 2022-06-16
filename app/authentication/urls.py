from django.urls import path
from authentication.views import ViewRegister, salir

urlpatterns = [
    path('registro/', ViewRegister.as_view(), name='register'),
    path('salir/', salir, name='logout'),
]
