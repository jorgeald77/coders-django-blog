from django.urls import path
from users.views import dashboard

urlpatterns = [
    path('mis-posts/', dashboard, name='dashboard'),
]
