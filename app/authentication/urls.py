from django.urls import path
from authentication.views import ViewRegister, salir, entrar

urlpatterns = [
    path('registro/', ViewRegister.as_view(), name='register'),
    path('logout/', salir, name='logout'),
    path('login/', entrar, name='login'),
]
