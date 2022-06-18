from django.urls import path
from profiles.views import ViewProfile

urlpatterns = [
    path('', ViewProfile.as_view(), name='profile'),
]
