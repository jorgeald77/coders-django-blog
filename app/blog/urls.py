from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
